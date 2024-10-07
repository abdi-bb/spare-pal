from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=50)  # Customer, Repair Shop, Business
    location = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name