from django.contrib import admin
from .models import Property, Tenant, Payment
# Register your models here.


admin.site.register(Property)
admin.site.register(Tenant)
admin.site.register(Payment)
