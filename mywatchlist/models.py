from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class myWatchListItem(models.Model):
    watched = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=255)
    review = models.CharField(max_length=255)
