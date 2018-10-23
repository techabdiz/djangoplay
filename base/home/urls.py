from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('rest', views.rest, name="rest"),
    path('download', views.download, name="download"),
]

