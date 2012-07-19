import markdown
from django.db import models
from taggit.managers import TaggableManager
from django.utils.safestring import mark_safe

class Song(models.Model):
    singer = models.ForeignKey('singers.Singer')
    content = models.TextField()
    title = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    tags = TaggableManager()
    
    def __unicode__(self):
        return '%s - %s' % (self.singer.user.username, self.date)
    
    @models.permalink
    def get_absolute_url(self):
        return ('show_song', [self.id])
    
    def send_tweet(self):
        """
        Send out a tweet to this user's twitter account announcing the new song.
        """
    
    def was_edited(self):
        """
        If the date modified and date created are more than two seconds apart...
        """
        if self.modified > self.date:
            d = (self.modified - self.date)
        else:
            d = (self.date - self.modified)
        
        return d.seconds > 2
    
    def rendered(self):
        return mark_safe(markdown.markdown(self.content, ['fenced_code']))