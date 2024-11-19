from django.shortcuts import render
from rest_framework import viewsets#, mixins
# from rest_framework.viewsets import GenericViewSet
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class Pagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100

# способ 1

# class NewsAPI(GenericViewSet,
#               mixins.CreateModelMixin,
#               mixins.RetrieveModelMixin,
#               mixins.UpdateModelMixin,
#               mixins.DestroyModelMixin):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer

# способ 2

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


