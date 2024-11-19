from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet

router = DefaultRouter()
router.register("recipes_viewSet", RecipeViewSet, basename='recipe-viewSet')

urlpatterns = [
    path('', include(router.urls)),
]
