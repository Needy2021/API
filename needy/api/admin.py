from django.contrib import admin

# Register your models here.

from .models import User, Offer, Image

admin.site.register(User)
admin.site.register(Offer)
admin.site.register(Image)
