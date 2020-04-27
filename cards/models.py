from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Card(models.Model):
    """
    This is going to be a single card being sold
    """
    MINT = 'M'
    NEAR_MINT = 'NM'
    EXCELLENT = 'EX'
    GOOD = 'GD'
    LIGHTLY_PLAYED = 'LP'
    PLAYED = 'PL'
    POOR = 'P'
    CARD_CONDITION_CHOICES = [
        (MINT, 'Mint'),
        (NEAR_MINT, 'Near Mint'),
        (EXCELLENT, 'Excellent'),
        (GOOD, 'Good'),
        (LIGHTLY_PLAYED, 'Lightly Played'),
        (PLAYED, 'Played'),
        (POOR, 'Poor'),
    ]

    card_title = models.CharField(max_length=200)
    card_description = models.TextField()
    card_edition = models.TextField()
    card_condition = models.CharField(
        max_length=2,
        choices=CARD_CONDITION_CHOICES,
        default=NEAR_MINT
    )
    card_price = models.DecimalField(max_digits=7, decimal_places=2, default='0.00')
    listing_created_date = models.DateTimeField(auto_now_add=True)
    listing_published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    listing_views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='0')

    def __unicode__(self):
        return self.title
