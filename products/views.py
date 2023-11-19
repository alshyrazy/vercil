from django.shortcuts import render
from .models import Car
# Create your views here.

def proind(request):
    x = {'pro' : Car.objects.all()}
    
    return render(request, 'products/products.html', x)