from song.models import Song
from annoying.decorators import render_to

@render_to('singer.html')
def singer_page(request, singer_id):
    songs = Song.objects.filter(singer__id=singer_id)
    return locals()