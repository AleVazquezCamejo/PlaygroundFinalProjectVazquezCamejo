from django.shortcuts import render, redirect
from django.http import HttpResponse
#para login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from myapp.forms import UserCreationFormCustom
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from myapp import forms, models
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def base(request):
    return render(request, 'base.html')


@login_required
def post(request):
    return render(request, 'post.html')

@login_required
def post1(request):
    return render(request, 'post1.html')

@login_required
def post2(request):
    return render(request, 'post2.html')

@login_required
def post3(request):
    return render(request, 'post3.html')


def contact(request):
    return render(request, 'contact.html')
    
    
def login_request(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data = request.POST)

    if form.is_valid():
      usuario = form.cleaned_data.get('username')
      contrasenia = form.cleaned_data.get('password')
      user = authenticate(username=usuario, password=contrasenia)

      login(request, user)
      return render(request, "index_mensaje.html", {"mensaje": f'Bienvenido {user.username}'})
  else:
    form = AuthenticationForm()
  return render(request, "login.html", {"form": form})


def registro(request):
   if request.method == 'POST':
       form = UserCreationFormCustom(request.POST)
       if form.is_valid():
           username = form.cleaned_data['username']
           form.save()

           return render(request, "index_mensaje.html", {"mensaje": "Usuario Creado"})
   else:
       form = UserCreationFormCustom()
       return render(request, "registro.html", {"form": form})
   
   
def logout_view(request):
    if request.method == "POST":
        logout(request)
        #return redirect("/myapp/Index")
        return render(request, "index_mensaje.html", {"mensaje": "Te has deslogueado"})
    return render(request, "logout.html")


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = forms.UserEditForm(request.POST, request.FILES, instance=request.user)
        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                if hasattr(usuario, 'avatar'):
                    usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.avatar.save()
                else:
                    models.Avatar.objects.create(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
            miFormulario.save()
            return render(request, "index.html")
    else:
        miFormulario = forms.UserEditForm(instance=request.user)
    return render(request, "editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})


class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = 'AppCoder/cambiar_clave.html'
    success_url = reverse_lazy('EditarPerfil')
