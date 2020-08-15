from django.shortcuts import render

# Create your views here.

from django_modelapiview import APIView

from .models import User, Offer, BasketItem, Message, Image

class UserView(APIView):
    model = User
    route = "users"


class OfferView(APIView):
    model = Offer
    route = "offers"


class BasketItemView(APIView):
    model = BasketItem
    route = "basketitems"


class MessageView(APIView):
    model = Message
    route = "messages"


class ImageView(APIView):
    model = Image
    route = "images"
