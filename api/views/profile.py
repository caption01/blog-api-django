from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from api.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = [
            'id',
            'name', 
            'email', 
            'bio', 
            'profile_image', 
            'social_github',
            'social_linkedin',
            'social_youtube',
            'social_website'
        ]

    def get_name(self, object):
        full_name = f'{object.first_name} {object.last_name}'
        return full_name

class ProfileView(APIView):
    """
    APIView to get and edit user profile
    ** Required token
    """
    http_method_names = ['get', 'put']
    permission_classes = [IsAuthenticated]

    def get(sef, request, pk=None, *arg, **kwarg):
        if pk is not None:
            profile = Profile.objects.filter(id=pk).first()
            serializer = ProfileSerializer(profile, many=False)
        else:
            profile = Profile.objects.all()
            serializer = ProfileSerializer(profile, many=True)
            
        return Response(serializer.data)

    def put(self, request, pk=None, format=None, *arg, **kwarg):
        user = request.user
        data = request.data

        if pk is None:
            error_message = {
                "message": "target id must provided"
            }
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        profile = Profile.objects.filter(id=pk).first()    
        
        if user != profile.user:
            error_message = {
                "message": "you have no permission"
            }
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProfileSerializer(profile, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

