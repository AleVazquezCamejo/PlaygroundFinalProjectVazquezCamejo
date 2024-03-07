from django.shortcuts import render
from django.http import HttpResponse
#para login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from myapp.forms import UserCreationFormCustom
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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

def post1(request):
    return render(request, 'post1.html')


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