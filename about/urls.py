from django.conf.urls import url
from django.contrib import admin
from .views import aboutView


urlpatterns = [
    url(r'', aboutView.as_view(), name="about"),
]