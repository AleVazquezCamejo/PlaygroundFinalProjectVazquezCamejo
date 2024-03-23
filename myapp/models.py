from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
class Mensaje(models.Model):
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f'Mensaje de {self.usuario.username} - {self.fecha_creacion}'
    
    
    