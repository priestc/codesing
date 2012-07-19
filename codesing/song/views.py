from annoying.decorators import render_to
from models import Song

@render_to('song.html')
def show_song(request, song_id):
    song = Song.objects.get(pk=song_id)
    return locals()