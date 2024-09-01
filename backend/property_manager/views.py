from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import PropertiesListSerializer, TenantSerializer, PaymentSerializer
from .models import Property, Tenant, Payment
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.


class PropertiesListCreateView(APIView):
    def get(self, request):
        user = request.user
        properties = Property.objects.filter(owner=user)
        serializer = PropertiesListSerializer(properties, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        data['owner'] = request.user.id
        serializer = PropertiesListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Property created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class propertyManagerView(APIView):
    def get(self, request, pk):
        user = request.user
        property = get_object_or_404(Property, pk=pk)
        if property.owner != user:
            return Response({"message": "You are not authorized to view this property"}, status=status.HTTP_403_FORBIDDEN)
        serializer = PropertiesListSerializer(property)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = request.user
        property = get_object_or_404(Property, pk=pk)
        if property.owner != user:
            return Response({"message": "You are not authorized to edit this property"}, status=status.HTTP_403_FORBIDDEN)
        serializer = PropertiesListSerializer(property, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = request.user
        property = get_object_or_404(Property, pk=pk)
        if property.owner != user:
            return Response({"message": "You are not authorized to delete this property"}, status=status.HTTP_403_FORBIDDEN)
        property.delete()
        return Response({"message": "Property deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    



class TenantsManagerView(APIView):
    def get(self, request, pk):
        user = request.user
        property = get_object_or_404(Property, pk=pk)
        if property.owner != user:
            return Response({"message": "You are not authorized to view tenants in this property"}, status=status.HTTP_403_FORBIDDEN)
        tenants = Tenant.objects.filter(property=property)
        serializer = TenantSerializer(tenants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        user = request.user
        property = get_object_or_404(Property, pk=pk)
        if property.owner != user:
            return Response({"message": "You are not authorized to add tenants to this property"}, status=status.HTTP_403_FORBIDDEN)
        data = request.data
        data['property'] = property.id
        serializer = TenantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Tenant added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class TenantView(APIView):
    def get(self, request, pk):
        user = request.user
        tenant = get_object_or_404(Tenant, id=pk)
        if tenant.property.owner != user:
            return Response({"message": "You are not authorized to view this tenant"}, status=status.HTTP_403_FORBIDDEN)
        serializer = TenantSerializer(tenant)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = request.user
        tenant = get_object_or_404(Tenant, id=pk)
        if tenant.property.owner != user:
            return Response({"message": "You are not authorized to edit this tenant"}, status=status.HTTP_403_FORBIDDEN)
        serializer = TenantSerializer(tenant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = request.user
        tenant = get_object_or_404(Tenant, id=pk)
        if tenant.property.owner != user:
            return Response({"message": "You are not authorized to delete this tenant"}, status=status.HTTP_403_FORBIDDEN)
        tenant.delete()
        return Response({"message": "Tenant deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    

class TenantPaymentView(APIView):
    def get(self, request, pk):
        user = request.user
        tenant = get_object_or_404(Tenant, id=pk)
        if tenant.property.owner != user:
            return Response({"message": "You are not authorized to view payments for this tenant"}, status=status.HTTP_403_FORBIDDEN)
        payments = Payment.objects.filter(tenant=tenant)
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk):
        user = request.user
        tenant = get_object_or_404(Tenant, id=pk)
        if tenant.property.owner != user:
            return Response({"message": "You are not authorized to add payments for this tenant"}, status=status.HTTP_403_FORBIDDEN)
        data = request.data
        data['tenant'] = tenant.id
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Payment added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class PaymentView(APIView):
    def get(self, request, pk):
        user = request.user
        payment = get_object_or_404(Payment, id=pk)
        if payment.tenant.property.owner != user:
            return Response({"message": "You are not authorized to view this payment"}, status=status.HTTP_403_FORBIDDEN)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        user = request.user
        payment = get_object_or_404(Payment, id=pk)
        if payment.tenant.property.owner != user:
            return Response({"message": "You are not authorized to edit this payment"}, status=status.HTTP_403_FORBIDDEN)
        serializer = PaymentSerializer(payment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = request.user
        payment = get_object_or_404(Payment, id=pk)
        if payment.tenant.property.owner != user:
            return Response({"message": "You are not authorized to delete this payment"}, status=status.HTTP_403_FORBIDDEN)
        payment.delete()
        return Response({"message": "Payment deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    


class TenantNotifyView(APIView):
    pass


    
    

