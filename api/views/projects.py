from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework import viewsets, serializers, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_access_policy import AccessPolicy

from api.models import Project, Tag, Profile

class ProjectsAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": "*",
            "effect": "allow"
        },
        {
            "action": ["create", 'update', 'destroy'],
            "principal": '*',
            "effect": "allow",
            "condition": "is_allow_create"
        }
    ]

    def is_allow_create(self, request, view, action):
        user = request.user
        isAuth = user.is_authenticated
        return isAuth

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
    permission_classes = (ProjectsAccessPolicy,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = {
    #     'title': ["exact"],
    #     'tags': ["exact", 'tags__name']
    # }
    search_fields = ['title', 'tags__name']

    def update_or_create_tags(self, tags):
        tag_list = []

        if tags is not None:
            for tag in tags:
                tag_obj, created = Tag.objects.get_or_create(name=tag)
                tag_list.append(tag_obj)
        
        return tag_list

    def create(self, request, *args, **kwargs):
        data = request.data
        tags = data.get('tags', None)
        user = request.user

        profile = Profile.objects.get(user=user)
        tag_list = self.update_or_create_tags(tags)

        project = Project.objects.create(
            owner=profile,
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

        if project is None:
            return Response({ "message": "project not found " }, status=status.HTTP_400_BAD_REQUEST)

        tag_list = self.update_or_create_tags(tags)

        project.title = data['title']
        project.description = data['description']
        project.link_url = data['link_url']
        project.tags.set(tag_list)
        
        project.save()
        serializer = self.serializer_class(project, many=False)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
