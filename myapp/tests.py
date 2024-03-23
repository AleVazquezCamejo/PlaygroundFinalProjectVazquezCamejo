from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.





class VerificarRutas(TestCase):
    def test_pagina_inicio(self):
        url = reverse('index')
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)
        
class LoginTestCase(TestCase):
    def setUp(self):
        self.username = 'usuario'
        self.password = 'contraseña'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        
    def test_login(self):
        #Realizar la solicitud POST al formulario de login
        response = self.client.post(reverse('Login'), {'username': self.username, 'password': self.password})
        #Comprobar que la respuesta es un redireccionamiento exitoso (HTTP 302)
        self.assertEqual(response.status_code, 200)
        #Comprobar que el usuario este autenticado
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        
    def test_login_invalid_credentials(self):
        #Intentar hacer login con credenciales invalidas
        response = self.client.post(reverse('Login'), {'username': 'usuario_invalido', 'password': 'contraseña_invalida'})
        #Comprobar que la respuesta no es un redireccionamiento (fallo el login)
        self.assertNotEqual(response.status_code, 302)
        #Comprobar que el usuario no esta autenticado
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        
        