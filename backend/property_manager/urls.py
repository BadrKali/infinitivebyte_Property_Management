from django.urls import path
from .views import PropertiesListCreateView, propertyManagerView, TenantsManagerView, TenantView, TenantPaymentView, PaymentView, TenantNotifyView

urlpatterns = [
    path('properties/', PropertiesListCreateView.as_view(), name='properties'),
    path('properties/<int:pk>/', propertyManagerView.as_view(), name='property'),
    path('properties/<int:pk>/tenants/', TenantsManagerView.as_view(), name='propertyTenants'),
    path('tenants/<int:pk>/', TenantView.as_view(), name='tenant'),
    path('tenants/<int:pk>/payments/', TenantPaymentView.as_view(), name='tenantsPayments'),
    path('payments/<int:pk>/', PaymentView.as_view(), name='payment'),
    path('tenants/<int:pk>/notify/', TenantNotifyView.as_view(), name='tenantNotify'),
]

