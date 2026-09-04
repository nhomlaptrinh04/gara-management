from django.contrib import admin
from .models import Customer, Vehicle, ServicePart, WorkOrder, OrderItem

admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(ServicePart)
admin.site.register(WorkOrder)
admin.site.register(OrderItem)
from django.contrib import admin
from .models import SparePart

@admin.register(SparePart)
class SparePartAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'quantity', 'price', 'updated_at')
    search_fields = ('name', 'code')