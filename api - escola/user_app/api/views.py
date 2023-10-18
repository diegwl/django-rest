from rest_framework.decorators import api_view

from rest_framework.permissions import AllowAny

from user_app.api.serializers import RegistrationSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from user_app import models

from rest_framework import status

class RegistrationView(APIView):
    permission_classes = (
        AllowAny,
    )
    def post(self, request):
        if request.method == 'POST':
            serializer = RegistrationSerializer(data=request.data)

            data = {}

            if serializer.is_valid():
                account = serializer.save()

                data['response'] = "Registration Successful"
                data['username'] = account.username
                data['email'] = account.email

                token = Token.objects.get(user=account).key
                data['token'] = token
            else:
                data = serializer.errors

            return Response(data)
        
class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        data = {"response": f"user {request.user.username} is logged out"}
        return Response(data, status=status.HTTP_200_OK)