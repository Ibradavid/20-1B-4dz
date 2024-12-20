from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(
        max_length=250
        )
    ingredients = models.TextField(
        )
    instructions = models.TextField(
        )
    prep_time = models.PositiveIntegerField(
        )
    is_vegetarian = models.BooleanField(
        default=False
        )
    created_at = models.DateTimeField(
        auto_now_add=True,
        )

    def __str__(self):
        return self.name
