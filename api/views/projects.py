from rest_framework import viewsets, serializers, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.models import Project
class ProjectSerializer(serializers.ModelSerializer):

    tags = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'image_url',
            'link_url',
            'tags',
            'created'
        ]

    def get_tags(self, object):
        tags = object.tags.all().values_list('name', flat=True).order_by('name')
        return tags

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
