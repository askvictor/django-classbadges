from school.models import SchoolClass, Student
from badger.models import Badge, Award
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
try:
    import django.utils.simplejson as json
except ImportError: # Django 1.5 no longer bundles simplejson
    import json


@staff_member_required
def class_badge_awards_view(request, class_code):
    #TODO - check access control - see which teachers teach this class
    c = SchoolClass.objects.get(code=class_code) #TODO - check cycle
    class_badges = []
    for b in c.subject.badges.all():
        class_badges.append(b)

    student_badge_awards = []
    for s in c.students.all():
        awards = []
        for i in range(len(class_badges)):
            if class_badges[i].is_awarded_to(s):
                awards.append(("award", class_badges[i].slug, Award.objects.get(user=s, badge=class_badges[i]).image.url))
            else:
                awards.append(("no_award", class_badges[i].slug, class_badges[i].image.url))
        student_badge_awards.append((s.username,awards))

    #get which of these badges have been awarded to these students
    return render_to_response('class_badge_awards.html',
                              {'student_badge_awards': student_badge_awards, 'class_badges':class_badges},
                              context_instance=RequestContext(request))
#@staff_member_required
def award_badge_view(request):
    if request.method=="POST" and request.is_ajax():
        b = get_object_or_404(Badge, slug=request.POST['badge'])
        s = get_object_or_404(Student, username=request.POST['student'])

        if request.POST['action'] == 'award':
            a = b.award_to(awardee=s, awarder=request.user) #TODO include class name in a note (when notes/comments implemented)
            if a:
                response = json.dumps({"awarded": "yes", "student":s.username, "badge":b.slug})
            else:
                response = json.dumps({"awarded": "no"})
            return HttpResponse(response, content_type="application/json")
        elif request.POST['action'] == 'unaward':
            a = get_object_or_404(Award, badge=b, user=s)
            a.delete()
            response = json.dumps({"unawarded": "yes", "student":s.username, "badge":b.slug})
            return HttpResponse(response, content_type="application/json")
