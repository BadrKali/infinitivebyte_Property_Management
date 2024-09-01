from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.




class Property(models.Model):
    name = models.CharField(max_length=255)
    property_image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    type = models.CharField(max_length=255)
    units = models.IntegerField()
    rental_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    


class Tenant(models.Model):
    name = models.CharField(max_length=255)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    


class Payment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateTimeField()
    is_settled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.tenant.name} paid {self.amount} on {self.date_paid}"