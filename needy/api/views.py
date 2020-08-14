from django.shortcuts import render

# Create your views here.

from django_modelapiview import APIView

from .models import User, Offer

class UserView(APIView):
    model = User
    route = "users"


class OfferView(APIView):
    model = Offer
    route = "offers"
