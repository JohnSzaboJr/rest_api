from rest_framework import generics, permissions
from .serializers import CitySerializer
from .models import City

class CreateView(generics.ListCreateAPIView):
    #handling POST, GET
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GetView(generics.ListAPIView):
    #handling GET
    queryset = City.objects.all()
    serializer_class = CitySerializer

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    #handling PUT, DELETE
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (permissions.IsAuthenticated,)
