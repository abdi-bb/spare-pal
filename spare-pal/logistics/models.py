from django.db import models

# Create your models here.

from orders.models import Order


class Logistic(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # tracking_number = models.CharField(max_length=100, unique=True)
    # status = models.CharField(max_length=100)  # In Transit, Delivered, etc.

    def __str__(self):
        return self.name