from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('Index', views.index, name="index"),
    path('About', views.about, name="about"),
    path('Base', views.base, name="base"),
    path('Post', views.post, name="post"),
    path('Post1', views.post1, name="post1"),
    path('Post2', views.post2, name="post2"),
    path('Post3', views.post3, name="post3"),
    path('Contact', views.contact, name="contact"),
    path('Login', views.login_request, name="Login"),
    path('Registro', views.registro, name="Registro"),
    #path('Logout', LogoutView.as_view(template_name='myapp/logout.html'), name='Logout'),
    path('Logout', views.logout_view, name="Logout"),
    path('EditarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('cambiarClave', views.CambiarClave.as_view(), name="CambiarClave"), 

]    

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)