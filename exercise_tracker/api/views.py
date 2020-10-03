from django.shortcuts import render

from rest_framework import viewsets

from .models import Users, Exercise
from .serializers import UserSerializer, ExerciseSerializer


class UsersView(viewsets.ModelViewSet):
    '''Viewset to provide CRUD for users'''
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class ExerciseView(viewsets.ModelViewSet):
    '''Viewset to provide CRUD for Exercise'''
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
