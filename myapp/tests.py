from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.





class VerificarRutas(TestCase):
    def test_pagina_inicio(self):
        url = reverse('Index')
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)