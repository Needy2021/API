from django.contrib import admin

# Register your models here.

from .models import User, Offer, Image, BasketItem, Message

admin.site.register(User)
admin.site.register(Offer)
admin.site.register(Image)
admin.site.register(BasketItem)
admin.site.register(Message)
