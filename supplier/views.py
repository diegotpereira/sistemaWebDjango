from django.shortcuts import render
from .models import Supplier

# Create your views here.
def supplier_list(request):
    suppliers = Supplier.objects.all()
    context = {
       'supplier_list': suppliers
    }
    return render(request, 'supplier/list.html', context)
