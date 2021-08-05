import re
from rest_framework import viewsets, serializers, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.models import Project, Tag
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

class ProjectsViewset(viewsets.ModelViewSet):
    """
    API endpoint for CRUD on Project Model.
    """

    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = Project.objects.all().order_by('-created')
    serializer_class = ProjectSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        tags = data.get('tags', None)

        tag_list = []

        if tags is not None:
            for tag in tags:
                tag_obj, created = Tag.objects.get_or_create(name=tag)
                tag_list.append(tag_obj)

        project = Project.objects.create(
            title=data['title'],
            description=data['description'],
            link_url=data['link_url'],
        )

        project.tags.set(tag_list)
        project.save()

        serializer = self.serializer_class(project, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk, *args, **kwargs):
        project = Project.objects.filter(id=pk).first()
        data = request.data
        tags = data.get('tags', None)
        tag_list = []

        if project is None:
            return Response({ "message": "project not found " }, status=status.HTTP_400_BAD_REQUEST)

        if tags is not None:
            for tag in tags:
                tag_obj, created = Tag.objects.get_or_create(name=tag)
                tag_list.append(tag_obj)

        project = Project.objects.create(
            title=data['title'],
            description=data['description'],
            link_url=data['link_url'],
        )

        project.tags.set(tag_list)
        project.save()
        serializer = self.serializer_class(project, many=False)

        return Response(serializer.data, status=status.HTTP_201_CREATED)