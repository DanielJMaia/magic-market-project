from django.db import models
from django.utils import timezone

class Card(models.Model):
    """
    This is going to be a single card being sold
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    edition = models.TextField()
    condition = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __unicode__(self):
        return self.title