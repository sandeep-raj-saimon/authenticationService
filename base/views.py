from django.http import HttpResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .utils import *
from .models import *
from .authentication_backends import *

# Create your views here.
def requestDataValidation(email, phone_number):
    if (email is None and phone_number is None):
        raise AssertionError("Email or Phone is mandatory")

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('get user')

    def post(self, request, *args, **kwargs):
        body = request.data
        phone_number = body["phoneNumber"] or None
        password = body["password"]
        email = body["email"] or None
        user_type = body["userType"] or 'CUSTOMER'

        try:
            requestDataValidation(email=email, phone_number=phone_number)
            if (email is None):
                User.objects.get(phone_number=phone_number)
            if (phone_number is None):
                User.objects.get(email=email)
            
            return CustomResponse(message="User exist with given email or phone number").error_response()
            
        except AssertionError as e:
            return HttpResponse(e)
        except Exception as e:
            current_user = User.objects.create_user(email=email, phone_number=phone_number, password=password, user_type=user_type)
            tokens = get_tokens_for_user(current_user)
            return CustomResponse(data=tokens).success_response()

    def update(self, request, *args, **kwargs):
        return HttpResponse('update user')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('delete user')

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        body = request.data
        phone_number = body.get("phoneNumber")
        password = body.get("password")
        email = body.get("email")

        try:
            requestDataValidation(email=email, phone_number=phone_number)
            if (email is None):
                current_user = User.objects.get(phone_number=phone_number)
            if (phone_number is None):
                current_user = User.objects.get(email=email)
            
            if current_user and AuthBackend().authenticate(request=request,email=email, password=password):
                tokens = get_tokens_for_user(current_user)
                return CustomResponse(data=tokens).success_response()
            else:
                return CustomResponse(message="Wrong password").error_response()
        except AssertionError as e:
            return CustomResponse(message=e).error_response()
        except Exception as e:
            print(e)
            return CustomResponse(message="User does not exist with given email or phone number").error_response()