from django.conf.urls import url
from django.contrib import admin
from .views import menuView, singleItem


urlpatterns = [
    url(r'^list/$', menuView.as_view(), name="menu"),
    url(r'^item/(?P<pk>[0-9]+)/$', singleItem.as_view(), name="single-item"),

]