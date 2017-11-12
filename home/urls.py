from django.conf.urls import url
from django.contrib import admin
from .views import homeView


urlpatterns = [
    url(r'$', homeView.as_view(), name="home"),
]