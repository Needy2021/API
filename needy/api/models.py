from django.db import models
from django.contrib.auth.models import AbstractUser

from django_modelapiview import JSONMixin

# Create your models here.

class User(JSONMixin, AbstractUser):
    """
    """

    json_fields= ['first_name', 'last_name', 'email', 'phone', 'offers', 'favorites', 'basket', 'messages_sent', 'messages_received']

    phone = models.CharField(max_length=15, blank=True, default="")
    # position = models. # Type to determine

    favorites = models.ManyToManyField("Offer", related_name="users")
    # tickets # Backref from Ticket user 1:N
    # basket # Backref from BasketItem user 1:N
    # messages_sent # Backref from Message user_from 1:N
    # messages_received # Backref from Message user_to 1:N


class Offer(JSONMixin, models.Model):
    """
    """

    json_fields = ['price', 'title', 'description', 'offeror', 'images', 'basketitems']

    price = models.IntegerField()
    title = models.CharField(max_length=128)
    description = models.TextField()
    # position = models. # Type to determine


    offeror = models.ForeignKey("User", on_delete=models.CASCADE, related_name="offers")
    # users # Backref from User favorites N:N
    # images # Backref from Image offer 1:N
    # basketitems # Backref from BasketItem offer 1:N


class Image(models.Model):
    """
     Used to store multiple images in one offer
    """

    image = models.ImageField()
    offer = models.ForeignKey("Offer", on_delete=models.CASCADE, related_name="images")


class BasketItem(JSONMixin, models.Model):
    """
     Store an offer associated with a user and a count
    """

    json_fields = ['count', 'user', 'offer']

    count = models.IntegerField(default=1)

    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="basket")
    offer = models.ForeignKey("Offer", on_delete=models.CASCADE, related_name="basketitems")


class Message(JSONMixin, models.Model):
    """
     Represent a conversion
    """

    json_fields = ['from_user', 'to_user', 'sent_at', 'body']

    from_user = models.ForeignKey("User", on_delete=models.SET_NULL, null=True, related_name="messages_sent")
    to_user = models.ForeignKey("User", on_delete=models.SET_NULL, null=True, related_name="messages_received")
    sent_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
