from django.shortcuts import render

from rest_framework import generics
from .serializers import UsersSerializer
from .models import Users

class CreateView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def perform_create(self, serializer):
        serializer.save()
