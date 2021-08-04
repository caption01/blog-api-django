import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from api.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileView(APIView):
    """
    APIView to get and edit user profile
    ** Required token
    """
    http_method_names = ['get', 'put']
    permission_classes = [IsAuthenticated]

    def get(sef, request, pk=None, *arg, **kwarg):
        user = request.user

        if pk is not None:
            profile = Profile.objects.filter(id=pk).first()
        else:
            profile = Profile.objects.filter(user=user).first()

        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None, *arg, **kwarg):
        user = request.user
        data = request.data

        if pk is not None:
            profile = Profile.objects.filter(id=pk).first()
        else:
            profile = Profile.objects.filter(user=user).first()
        
        serializer = ProfileSerializer(profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

