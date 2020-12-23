from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=150, blank=True)
 
    def __str__(self):
        return self.name