from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Flight(models.Model):
    origin = CharField (max_length=64)
    destination = CharField (max_length=64)
    duration =models.IntegerField()