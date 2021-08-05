from rest_framework import viewsets, serializers, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'image_url',
            'link_url',
            'created'
        ]

class ProjectsViewset(viewsets.ViewSet):
    """
    API endpoint for CRUD on Project Model.
    """

    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
