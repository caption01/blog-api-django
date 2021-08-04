from django.conf.urls import url
from django.urls import path
from .views.profile import ProfileView

urlpatterns = [
    url(r'^profile(?:/(?P<pk>[^/.]+))?/?', ProfileView.as_view())
]