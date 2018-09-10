from django.test import TestCase
from .models import City
from django.contrib.auth.models import User

class ModelTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username="nerd")
        self.city_name = "Test"
        self.city = City(name=self.city_name, population=1, owner=user)

    def test_model_can_create_a_city(self):
        # Testing if we can create an item in db
        old_count = City.objects.count()
        self.city.save()
        new_count = City.objects.count()
        self.assertNotEqual(old_count, new_count)