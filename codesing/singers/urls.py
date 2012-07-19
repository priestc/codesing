from django.conf.urls import patterns, include, url

urlpatterns = patterns('singers.views',
    url(r'^songs/(?P<singer_id>\d+)', 'singer_page', name='singer_page'),
)