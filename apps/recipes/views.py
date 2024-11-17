from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from .models import Recipe
from .serializers import RecipeSerializer

# Create your views here.


class NewsAPI(GenericViewSet,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


