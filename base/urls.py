from django.urls import path
from django.http import HttpResponse
from .views import *

def home(request):
    return HttpResponse("Home Page")

urlpatterns = [
    path("", home, name = "home"),
    path("user/", UserView.as_view()),
    path("login/", LoginView.as_view())
]