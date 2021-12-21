from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.query_utils import check_rel_lookup_compatibility

# Create your models here.

class Airport(models.Model):
    code = models.CharField (max_length=3)
    city = models.CharField (max_length=64)
    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey (Airport, on_delete= CASCADE, related_name="departures")
    destination = models.ForeignKey (Airport, on_delete= CASCADE, related_name="arrivals")
    duration =models.IntegerField()
    
    def __str__(self):
      return f"{self.id}: {self.origin} to {self.destination}"
