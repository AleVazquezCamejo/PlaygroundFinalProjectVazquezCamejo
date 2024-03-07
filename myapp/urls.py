from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('Index', views.index, name="index"),
    path('About', views.about, name="about"),
    path('Base', views.base, name="base"),
    path('Post', views.post, name="post"),
    path('Post1', views.post1, name="post1"),
    path('Contact', views.contact, name="contact"),
    path('Login', views.login_request, name="Login"),
    path('Registro', views.registro, name="Registro"),
    path('Logout', LogoutView.as_view(template_name='myapp/logout.html'), name='Logout'),
    

]    