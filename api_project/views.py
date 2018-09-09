from rest_framework import generics
from .serializers import CitySerializer
from .models import City

class CreateView(generics.ListCreateAPIView):
    #handling POST
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    #handling GET, PUT, DELETE
    queryset = City.objects.all()
    serializer_class = CitySerializer
