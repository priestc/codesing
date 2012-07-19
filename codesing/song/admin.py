from django.contrib import admin
from models import Song

class SongAdmin(admin.ModelAdmin):
    pass
    #list_display = ()
    #search_fields = ()
    #list_filter = ()
    
admin.site.register(Song, SongAdmin)