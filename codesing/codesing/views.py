from annoying.decorators import render_to
from song.models import Song

@render_to('home.html')
def home(request):
    latest_songs = Song.objects.order_by('date')[:15]
    return locals()
    

def logout(request):
    pass