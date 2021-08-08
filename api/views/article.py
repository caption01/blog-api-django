from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework import viewsets, serializers, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_access_policy import AccessPolicy

from api.models import Article, Profile

class ArticleAccessPolicy(AccessPolicy):
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

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'description',
            'link_medium',
            'link_fb',
            'link_youtube',
            'created'
        ]

class ArticleViewset(viewsets.ModelViewSet):
    """
    API endpoint for CRUD on Project Model.
    """

    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = Article.objects.all().order_by('-created')
    serializer_class = ArticleSerializer
    permission_classes = (ArticleAccessPolicy,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'description']

    def create(self, request, *args, **kwargs):
        user = request.user
        profile = Profile.objects.get(user=user)
        data = request.data

        article = Article.objects.create(
            owner = profile,
            title = data.get('title'),
            description = data.get('description'),
            image_url = data.get('image_url'),
            link_medium = data.get('link_medium'),
            link_fb = data.get('link_fb'),
            link_youtube = data.get('link_youtube'),
        )

        article.save()
        serializer = self.serializer_class(article, many=False)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
