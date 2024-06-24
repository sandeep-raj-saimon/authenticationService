from rest_framework.response import Response
from rest_framework import status
class CustomResponse:

    def __init__(self, data=None, message=None):
        self.data = data
        self.message = message

    def success_response(self):
        return Response({
            "data": self.data,
            "message": self.message
        }, status=status.HTTP_200_OK)

    def error_response(self):
        return Response({
            "data": self.data,
            "message": self.message
        }, status=status.HTTP_400_BAD_REQUEST)