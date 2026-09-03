from django.shortcuts import render, redirect
from .models import Customer, WorkOrder, Vehicle
from .forms import CustomerForm, WorkOrderForm

def dashboard(request):
    orders = WorkOrder.objects.all().order_by('-created_at')[:5]
    context = {
        'total_customers': Customer.objects.count(),
        'total_vehicles': Vehicle.objects.count(),
        'active_orders': WorkOrder.objects.exclude(status='DONE').count(),
        'recent_orders': orders
    }
    return render(request, 'dashboard.html', context)

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def order_create(request):
    if request.method == 'POST':
        form = WorkOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = WorkOrderForm()
    return render(request, 'form_template.html', {'form': form, 'title': 'Tạo Lệnh Sửa Chữa Mới'})
