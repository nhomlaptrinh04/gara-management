from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('customers/', views.customer_list, name='customer_list'),
    path('orders/new/', views.order_create, name='order_create'),
    path('inventory/', views.inventory_view, name='inventory'),
    path('inventory/add/', views.inventory_add, name='inventory_add'),
]

