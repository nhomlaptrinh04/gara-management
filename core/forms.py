from django import forms
from .models import Customer, Vehicle, WorkOrder

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = ['vehicle', 'mechanic', 'description', 'status']
        widgets = {
            'vehicle': forms.Select(attrs={'class': 'form-select'}),
            'mechanic': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
        from django import forms
from .models import SparePart

class SparePartForm(forms.ModelForm):
    class Meta:
        model = SparePart
        fields = ['code', 'name', 'quantity', 'price']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập mã linh kiện'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập tên linh kiện'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }