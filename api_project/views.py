# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    views.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jszabo <jszabo@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/08 16:53:31 by jszabo            #+#    #+#              #
#    Updated: 2018/09/08 17:06:26 by jszabo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from django.shortcuts import render

from rest_framework import generics
from .serializers import UsersSerializer
from .models import Users

class CreateView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Users.objects.all()
    serializer_class = UsersSerializer
