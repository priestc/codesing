from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codesing.views.home', name='home'),
    # url(r'^codesing/', include('codesing.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^songs', include('song.urls')),
    (r'^singers', include('singers.urls')),
    
    (r'^$', redirect_to, {'url': '/home'}),
    (r'^home', 'codesing.views.home'),
    
    url(r'logout', 'codesing.views.logout', name='logout'),
    
    
)
