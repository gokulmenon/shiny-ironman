from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = patterns('',
    # GAE warmup request
    url(r'^_ah/warmup$',
       TemplateView.as_view(template_name='warmup.html'),
       name='warmup'),

    # admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^', include('home.urls', namespace='home')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^application/', include('applications.urls', namespace='applications')),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^user/', include('custom_user.urls', namespace='users')),
    url(r'^portfolio/', include('portfolios.urls', namespace='portfolios')),
    url(r'^project/', include('projects.urls', namespace='projects')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )