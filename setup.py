from setuptools import setup, find_packages


setup(
    name='django-classbadges',
    version='0.0.1',
    description='badge awarding system for schools',
    long_description=open('README.md').read(),
    author='Victor Rajewski',
    author_email='askvictor@gmail.com',
    url='http://github.com/askvictor/django-classbadges',
    license='BSD',
    packages=find_packages(),
    package_data={'': ['*.html','*.txt','*.js']},
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
