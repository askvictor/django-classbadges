from django.conf.urls import patterns, url

urlpatterns = patterns('class_badges.views',
    url(r'^(?P<class_code>[^/]+)/badges/$','class_badge_awards_view'),
    url(r'^action/$','award_badge_view'),
)