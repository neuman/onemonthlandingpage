from django.db import models
from geoposition.fields import GeopositionField
from django.core.urlresolvers import reverse
import uuid
import os

# Create your models here.

APPNAME = 'core'

CATEGORY_CHOICES = (
    ('R', 'Restaurant'),
    ('B', 'Bar'),
    ('F', 'Fast Food'),
    ('V', 'Venue')
)

def get_file_path(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('uploads/', filename)

class Location(models.Model):
    title = models.TextField()
    position = GeopositionField()
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    image_file = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_image_url(self):
        if self.image_file != None:
            return self.image_file.url.replace("https", "http")
        else:
            return None

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname='location_detail', args=[self.id], current_app=APPNAME)