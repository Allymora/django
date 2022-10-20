from django.db import models

# Create your models here.

class Airport(models.Model): 
    code= models.CharField(max_length=3)
    city= models.CharField(max_length=50)

    def __str__(self):
        return f'{self.code}, {self.city}'

class Flights(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.IntegerField()

    def __str__(self): 
        return f'{self.id} - {self.origin} hacia {self.destination}' 