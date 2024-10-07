from django.db import models

# Create your models here.

from suppliers.models import Supplier

class Part(models.Model):
    name = models.CharField(max_length=255)
    part_number = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    stock_quantity = models.IntegerField()

    def __str__(self):
        return self.name