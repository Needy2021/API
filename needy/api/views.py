from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import get_resolver
from django.db.models import Func, F

import json
from http import HTTPStatus
from math import cos, asin, sqrt, pi

from django_modelapiview import APIView, Token
from django_modelapiview.responses import APIResponse

# Create your views here.

from .models import User, Offer, BasketItem, Message, Image, Comment

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
            return APIResponse(HTTPStatus.OK, "User logged in", {'token': str(token), 'user': user.serialize(request)})
        else:
            return APIResponse(HTTPStatus.UNAUTHORIZED, "Wrong user credentials")

class UserView(APIView):
    model = User
    route = "users"


class OfferView(APIView):
    model = Offer
    route = "offers"

    def get(self, request, *args, **kwargs):
        if 'distance' in request.GET:
            distance =  request.GET.pop('distance')
            if not 'user' in request.GET:
                return APIResponse(HTTPStatus.BAD_REQUEST, "distance lookup needs the user lookup")
            user_id = request.GET.pop('user')
            user = User.objects.get(id=user_id)
            # p = pi/180
            # a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
            # offer_distance = 12742 * asin(sqrt(a)) #2*R*asin...
            self.queryset = self.queryset.annotate(distance=Func(F('latitude') - user.latitude, function='ABS') + Func(F('longitude') - user.longitude, function='ABS')).filter(distance__lte=distance)
        return super().get(request, *args, **kwargs)


class BasketItemView(APIView):
    model = BasketItem
    route = "basketitems"


class MessageView(APIView):
    model = Message
    route = "messages"


class ImageView(APIView):
    model = Image
    route = "images"


class CommentView(APIView):
    model = Comment
    route = "comments"
