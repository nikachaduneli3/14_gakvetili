from django.shortcuts import render, redirect
from .forms import  ProductForm
from .models import  Product


def index(request):
    form = ProductForm()
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    return render(request, 'index.html',
                  {'form':form, 'products':products})

