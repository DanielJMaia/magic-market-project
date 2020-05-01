from django.db import models
from cards.models import Card
from django.contrib.auth.models import User


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return "Order ID: {0} - Date: {1}- Customer Name: {2} - Customer Username: {3}".format(self.id, self.date, self.full_name, self.user.username)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    card = models.ForeignKey(Card, null=False)
    quantity = models.IntegerField(blank=False)

    def __str(self):
        return "{0} {1} @ {2}".format(self.quantity, self.card.name, self.card.price)
