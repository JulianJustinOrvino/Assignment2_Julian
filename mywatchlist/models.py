from django.db import models

class MyWatchListItem(models.Model):
    watched = models.TextField()
    title = models.TextField()
    release_date = models.CharField(max_length=255)
    rating = models.IntegerField()
    review = models.TextField()
    