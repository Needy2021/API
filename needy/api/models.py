from django.db import models
from django.contrib.auth.models import AbstractUser

from django_modelapiview import JSONMixin

# Create your models here.

class User(JSONMixin, AbstractUser):
    """
    """

    json_fields= ['first_name', 'last_name', 'email', 'phone']

    phone = models.CharField(max_length=15, blank=True, default="")
    # position = models. # Type to determine

    favorites = models.ManyToManyField("Offer", related_name="users")
    # messages # Backref from Message user 1:N
    # tickets # Backref from Ticket user 1:N


class Offer(JSONMixin, models.Model):
    """
    """

    json_fields = ['price', 'title', 'description', 'offeror']

    price = models.IntegerField()
    title = models.CharField(max_length=128)
    description = models.TextField()
    # position = models. # Type to determine


    offeror = models.ForeignKey("User", on_delete=models.CASCADE, related_name="offers")
    # users # Backref from User favorites N:N
    # images # Backref from Image offer 1:N


class Image(models.Model):
    """
     Used to store multiple images in one offer
    """

    image = models.ImageField()
    offer = models.ForeignKey("Offer", on_delete=models.CASCADE, related_name="images")
