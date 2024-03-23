from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserModel, UserChangeForm
from django.contrib.auth.models import User
from .models import Mensaje


class UserCreationFormCustom(UserCreationForm):
  user = forms.TextInput()
  email = forms.EmailField()
  password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
#   class Meta:
#       model = UserModel
#       fields = ['username', 'email', 'password1', 'password2']
#       #saca los mensajes de ayuda
#       help_text = {k:"" for k in fields}
      


class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    imagen = forms.ImageField(label="Avatar", required=False)
    
    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'imagen']      
        

class MensajeForm(forms.ModelForm):
  class Meta:
    model = Mensaje
    fields = ['nombre', 'email', 'phone', 'contenido']
    
  nombre = forms.CharField(max_length=100)
  phone = forms.CharField(max_length=12)
  email = forms.EmailField()
  