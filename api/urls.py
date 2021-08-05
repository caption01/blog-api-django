from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

from .views.login import LoginView
from .views.profile import ProfileView
from .views.projects import ProjectsViewset

router = routers.DefaultRouter()
router.register('projects', ProjectsViewset)

urlpatterns = [
    url(r'login/?', LoginView.as_view()),
    url(r'^profile(?:/(?P<pk>[^/.]+))?/?', ProfileView.as_view()),
    path('', include(router.urls))
]