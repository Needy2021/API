from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import get_resolver

import json
from http import HTTPStatus

from django_modelapiview import APIView, Token
from django_modelapiview.responses import APIResponse

# Create your views here.

from .models import User, Offer, BasketItem, Message, Image

class URLsView(View):
    def get(self, request, **kwargs):
        return APIResponse(HTTPStatus.OK, "URLs available", list(set(v[1] for v in get_resolver(None).reverse_dict.values())))

@method_decorator(csrf_exempt, "dispatch")
class LoginView(View):
    def post(self, request, **kwargs):
        data = request.body.decode('utf-8')
        json_data = json.loads(data)

        user = authenticate(username=json_data['username'], password=json_data['password'])
        if user is not None:
            token = Token({'uid': user.id})
            token.sign()
            return APIResponse(HTTPStatus.OK, "User logged in", str(token))
        else:
            return APIResponse(HTTPStatus.UNAUTHORIZED, "Wrong user credentials")

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
