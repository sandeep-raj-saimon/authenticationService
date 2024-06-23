from .models import *
from django.contrib.auth.backends import BaseBackend
def authenticate(request, email, phone_number, password=None):
    if (email):
        user = User.objects.get(email=email)

    if (phone_number):
        user = User.objects.get(phone_number=phone_number)
    if user.check_password(password):
        return user
    return None

class AuthBackend(BaseBackend):
    def authenticate(self, request, email, phone_number, password, **kwargs):
        if (phone_number is None and email is None):
            raise ValueError('Email or Phone Number must be provided')
        return authenticate(request, email, phone_number, password)