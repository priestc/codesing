from django.contrib import admin
from models import Singer

class SingerAdmin(admin.ModelAdmin):
    pass
    #list_display = ()
    #search_fields = ()
    #list_filter = ()
    
admin.site.register(Singer, SingerAdmin)