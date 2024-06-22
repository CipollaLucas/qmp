from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Creamos un test para probar la signal de la creación de usuiario y perfil
class ProfileTestCase(TestCase):
    def setUp(self): # Preparamos la prueba, los parametros
        User.objects.create_user('test', 'test@test.com', 'test1234')


    def test_profile_exists(self): # Ejecutamos la pruebba
        exists = Profile.objects.filter(user__username='test').exists() # buscamos a ver si existe, retorna booleanos
        self.assertEqual(exists, True)


