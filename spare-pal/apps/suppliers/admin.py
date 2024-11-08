from django.contrib import admin

# Register your models here.

from apps.suppliers.models import Supplier

admin.site.register(Supplier)