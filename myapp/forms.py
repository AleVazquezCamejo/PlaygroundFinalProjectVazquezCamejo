from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserModel



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
      
