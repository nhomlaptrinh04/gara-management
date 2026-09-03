from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Tên khách hàng")
    phone = models.CharField(max_length=20, unique=True, verbose_name="Số điện thoại")
    address = models.CharField(max_length=255, blank=True, verbose_name="Địa chỉ")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.name

class Vehicle(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=20, unique=True, verbose_name="Biển số")
    brand = models.CharField(max_length=50, verbose_name="Hãng xe")
    model_name = models.CharField(max_length=50, verbose_name="Dòng xe")

    def __str__(self): return f"{self.license_plate} ({self.customer.name})"

class ServicePart(models.Model):
    name = models.CharField(max_length=200, verbose_name="Tên Phụ tùng / Dịch vụ")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Đơn giá (VNĐ)")
    is_part = models.BooleanField(default=True, verbose_name="Là phụ tùng")
    stock = models.IntegerField(default=0, verbose_name="Tồn kho")

    def __str__(self): return self.name

class WorkOrder(models.Model):
    STATUS = (('WAIT', 'Chờ xử lý'), ('DOING', 'Đang sửa'), ('DONE', 'Hoàn thành'))
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(verbose_name="Tình trạng xe")
    status = models.CharField(max_length=10, choices=STATUS, default='WAIT')
    created_at = models.DateTimeField(auto_now_add=True)

    def total_cost(self):
        return sum(item.total_price() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(WorkOrder, related_name='items', on_delete=models.CASCADE)
    service_part = models.ForeignKey(ServicePart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.quantity * self.service_part.price