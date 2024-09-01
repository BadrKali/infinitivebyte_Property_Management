from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Property, Tenant, Payment

User = get_user_model()



class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'



class PropertiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

    def validate_rental_cost(self, rental_cost):
        if rental_cost < 0:
            raise serializers.ValidationError("Rental cost cannot be a negative number.")
        return rental_cost

    def validate_units(self, units):
        if units < 0:
            raise serializers.ValidationError("Units cannot be a negative number.")
        return units


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'