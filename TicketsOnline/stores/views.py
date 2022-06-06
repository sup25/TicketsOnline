from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def stores(request):
    context = {}
    return render(request, 'stores/stores.html', context)

def carts(request):
    context = {}
    return render(request, 'stores/carts.html', context)

def checkout(request):
    context = {}
    return render(request, 'stores/checkout.html', context)



