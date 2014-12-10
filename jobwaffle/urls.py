from django.conf.urls import patterns, include, url
from django.conf import settings  # Need for static content
from django.contrib.auth import views as auth_views
from django.contrib import admin
#from rest_framework import routers


from applicant.views import Base, ResumeCreateView, ResumeListView, \
    ResumeUpdateView, ResumeDeleteView, Profile
from employer.views import JobCreateView, JobListView, \
    JobSearchView, JobPostView, JobUpdateView, JobDeleteView

admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf
#router = routers.DefaultRouter()
#router.register(r'resume', resumeViewSet)


urlpatterns = patterns('',

    # Examples:
    #url(r'^$', 'jobwaffle.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^$", Base.as_view(), name="base"),  # Home Page

    ###### SOCIAL REGISTRATION with django-allauth
    # prevent extra are you sure logout step
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}),

    url(r"^accounts/", include("allauth.urls")),  # django-allauth

    ###### RESUMES

    # Create Resume
    url(r"^resume_create$", ResumeCreateView.as_view(), name="resume-create"),

    # List Specific Resume
    url(r'^profile/(?P<username>[-\w\d]+)/(?P<pk>\d+)/$',
        ResumeListView.as_view(), name="resume-list"),

    # Update Specific Resume
    url(r'^profile/(?P<username>\w+)/update/(?P<pk>\d+)/$',
        ResumeUpdateView.as_view(), name="resume-update"),

    # Delete Specific Resume
    url(r'^profile/(?P<username>\w+)/delete/(?P<pk>\d+)/$',
        ResumeDeleteView.as_view(), name="resume-delete"),

    #url(r"^resume_view$", .as_view() , name="resume-view"),

    ###### JOBS

    url(r"^jobsearch$", JobSearchView.as_view(), name="job-search"),  # Home Page

    # All Job Listing Page
    url(r"^job_all$", JobListView.as_view(), name="job-all"),

    # Create Job post
    url(r"^job_create$", JobCreateView.as_view(), name="job-create"),

    # List all your job posts
    url(r'^job_post$', JobPostView.as_view(), name='job-post'),

    # List Specific Job
    url(r'^job/list/(?P<pk>\d+)/$', JobListView.as_view(), name='job-list'),

    # Update Specific Job
    url(r'^job/update/(?P<pk>\d+)/$', JobUpdateView.as_view(), name='job-update'),

    # Delete Specific Job
    url(r'^job/delete/(?P<pk>\d+)/$', JobDeleteView.as_view(), name='job-delete'),


    # STATIC and MEDIA paths
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),

    # User Profile Page
    url(r'^profile/(?P<username>\w+)/$', Profile.as_view(),
        name="profile"),  # Profile Page


    url(r'^admin/', include(admin.site.urls)),
)
