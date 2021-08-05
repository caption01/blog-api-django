from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User

from api.models import Profile

class LoginView(APIView):
    """
    this is endpoint for user login and get a token.
    """

    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = request.data
        data_username = data['username']
        data_password = data['password']

        try:
            user = User.objects.get(username=data_username)
        except User.DoesNotExist:
            error_message = {
                "message": "username not found"
            }
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        try:
            if user.check_password(data_password):
                token, created = Token.objects.get_or_create(user=user)
                profile = Profile.objects.get(user=user)
                return Response({ 
                    'token': token.key,
                    'profile_id': profile.id, 
                    }, status=status.HTTP_200_OK
                )
        except Exception as e:
            print('Intenal error', e)
            error_message = {
                "message": "something went wrong, please try again"
            }
            return Response(error_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        error_message = {
                "message": "In valid username or password"
        }
        return Response(error_message, status=status.HTTP_400_BAD_REQUEST)