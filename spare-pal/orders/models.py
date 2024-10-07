from django.db import models

# Create your models here.

from customers.models import Customer
from parts.models import Part


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    # quantity = models.IntegerField()
    status = models.CharField(max_length=50, default='Pending')  # Pending, Processing, Shipped, Delivered

    def __str__(self):
        return f'Order {self.id} by {self.customer.name} for {self.part.name}'