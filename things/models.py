from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    name = models.CharField(unique=True,blank=False,max_length=30)
    description = models.CharField(unique=False,max_length=120, blank=True)
    quantity = models.IntegerField(unique=False,validators=[MinValueValidator(0), MaxValueValidator(100)])