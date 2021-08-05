from django.conf.urls import url
from django.urls import path
from .views.profile import ProfileView
from .views.login import LoginView

urlpatterns = [
    url(r'login/?', LoginView.as_view()),
    url(r'^profile(?:/(?P<pk>[^/.]+))?/?', ProfileView.as_view())
]