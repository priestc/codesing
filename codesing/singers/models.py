from django.db import models

# Create your models here.

class Singer(models.Model):
    user = models.ForeignKey('auth.User')
    twitter_name = models.CharField(max_length=64, blank=True)
    
    def __unicode__(self):
        return self.user.username
    
    @models.permalink
    def get_absolute_url(self):
        return ('singer_page', [self.pk])