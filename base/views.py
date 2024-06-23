from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import *
from .authentication_backends import *

# Create your views here.
class UserView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('get user')

    def post(self, request, *args, **kwargs):
        return HttpResponse('post user')

    def update(self, request, *args, **kwargs):
        return HttpResponse('update user')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('delete user')

class LoginView(View):
    def post(self, request, *args, **kwargs):
        return HttpResponse('User login')