from django.db import models
from geoposition.fields import GeopositionField
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Avg
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

RATING_CHOICES = (
    (0, 'None'),
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****')
)

def get_file_path(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('uploads/', filename)

class Location(models.Model):
    title = category = models.CharField(max_length=300)
    position = GeopositionField()
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    image_file = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_image_url(self):
        if self.image_file.name != '':
            return self.image_file.url.replace("https", "http")
        else:
            return None

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname='location_detail', args=[self.id], current_app=APPNAME)

    def get_average_rating(self):
        return self.review_set.all().aggregate(Avg('rating'))['rating__avg']

    def get_pretty_rating(self):
        count = self.review_set.all().count()
        if count==0:
            return "No Ratings Yet"
        else:
            return "Average Rating of "+str(self.get_average_rating())+" From "+str(count)+" Reviews"

class Review(models.Model):
    location = models.ForeignKey(Location)
    user = models.ForeignKey(User)
    description = models.TextField(null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("user", "location"),)