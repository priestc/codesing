from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/(?P<song_id>\d+)', 'song.views.show_song', name="show_song"),
)