from django.db import models

# Create your models here.
class Dish(models.Model):
    item = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.item
