from django.conf.urls import url
from django.contrib import admin
from .views import cateringView

urlpatterns = [
    url(r'', cateringView.as_view(), name="catering"),
]