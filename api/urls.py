from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

from .views.login import LoginView
from .views.profile import ProfileView
from .views.projects import ProjectsViewset
from .views.article import ArticleViewset

router = routers.DefaultRouter()
router.register('projects', ProjectsViewset)
router.register('articles', ArticleViewset)

urlpatterns = [
    url(r'login/?', LoginView.as_view()),
    url(r'^profile(?:/(?P<pk>[^/.]+))?/?', ProfileView.as_view()),
    path('', include(router.urls))
]