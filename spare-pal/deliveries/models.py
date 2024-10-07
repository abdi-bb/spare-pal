from django.db import models

# Create your models here.

from orders.models import Order
from logistics.models import Logistic

class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='delivery')
    logistic = models.ForeignKey(Logistic, on_delete=models.CASCADE, related_name='deliveries')
    delivery_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default='In Transit')

    def __str__(self):
        return f"Delivery for Order {self.order.id} by {self.logistic.name}"