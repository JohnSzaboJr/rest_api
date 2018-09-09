from django.test import TestCase
from django.contrib.auth.models import User
#from .models import City

class ModelTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username="default")
    self.name = "Something"
        self.city = City(name=self.name, owner=user)
