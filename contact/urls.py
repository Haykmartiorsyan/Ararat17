from django.conf.urls import url
from django.contrib import admin
from .views import contactView


urlpatterns = [
    url(r'', contactView.as_view(), name="contact"),
]