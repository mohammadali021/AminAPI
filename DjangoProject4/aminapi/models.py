from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=1000)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name

