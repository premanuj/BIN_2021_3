from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    in_stock = models.BooleanField(default=True)