from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

from django_modelapiview import JSONMixin

# Create your models here.

class User(JSONMixin, AbstractUser):
    """
    """

    json_fields = ['username', 'password', 'first_name', 'last_name', 'email', 'phone', 'rating', 'latitude', 'longitude', 'offers', 'favorites', 'basket', 'messages_sent', 'messages_received', 'comments']

    phone = models.CharField(max_length=15, blank=True, default="")
    rating = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    favorites = models.ManyToManyField("Offer", related_name="users", blank=True)
    # tickets # Backref from Ticket user 1:N
    # basket # Backref from BasketItem user 1:N
    # messages_sent # Backref from Message user_from 1:N
    # messages_received # Backref from Message user_to 1:N
    # commments # Backref from Comment user 1:N

    def save(self, *args, **kwargs):
        if not "_" in self.password:
            self.set_password(self.password)
        super().save(*args, **kwargs)


class Offer(JSONMixin, models.Model):
    """
    """

    json_fields = ['price', 'title', 'description', 'latitude', 'longitude', 'offeror', 'images', 'comments']

    price = models.IntegerField()
    title = models.CharField(max_length=128)
    description = models.TextField()
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    offeror = models.ForeignKey("User", on_delete=models.CASCADE, related_name="offers")
    # users # Backref from User favorites N:N
    # images # Backref from Image offer 1:N
    # basketitems # Backref from BasketItem offer 1:N
    # comments # Backref from Comment offer 1:N


class Image(JSONMixin, models.Model):
    """
     Used to store multiple images in one offer
    """

    json_fields = ['image', 'offer']

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


class Comment(JSONMixin, models.Model):
    """
     User comment on an offer
    """

    json_fields = ['body', 'offer', 'user']

    body = models.TextField()

    offer = models.ForeignKey("Offer", on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="comments")
