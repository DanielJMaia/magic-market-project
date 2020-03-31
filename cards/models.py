from django.db import models
from django.utils import timezone

class Card(models.Model):
    """
    This is going to be a single card being sold
    """
    card_title = models.CharField(max_length=200)
    card_description = models.TextField()
    card_edition = models.TextField()
    card_condition = models.TextField()
    card_price = models.DecimalField(max_digits=7, decimal_places=2, default='0')
    listing_created_date = models.DateTimeField(auto_now_add=True)
    listing_published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    listing_views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    
    def __unicode__(self):
        return self.title