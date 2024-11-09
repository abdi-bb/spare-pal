from django.contrib import admin

# Register your models here.

from apps.companies.models import Company

admin.site.register(Company)