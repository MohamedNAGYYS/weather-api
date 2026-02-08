from django.db import models
from django.contrib.auth.models import User

class Weather(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    wind_speed = models.CharField(max_length=10,null=True, blank=True) 
    humidity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.city
    