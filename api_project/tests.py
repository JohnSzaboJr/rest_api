from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import City
from .serializers import CitySerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_city(name="", population=""):
        if name != "" and population != "":
            City.objects.create(name=name, population=population)

    def setUp(self):
        # add test data
        self.create_city("Shanghai", "24115000")

class GetAllCitiesTest(BaseViewTest):

    def test_get_all_cities(self):
        """
        This test ensures that all cities added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("cities-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = City.objects.all()
        serialized = CitySerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)