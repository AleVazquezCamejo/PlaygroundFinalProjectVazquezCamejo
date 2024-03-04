from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Index', views.index, name="index"),
    path('About', views.about, name="about"),
]    