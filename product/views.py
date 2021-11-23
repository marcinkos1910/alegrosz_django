from django.shortcuts import render, get_object_or_404, redirect

from product.forms import ProductForm
from product.models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {"products": products})


def product(request, pk):
    item = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product.html', {"product": item})


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'product/create_product.html', {"form": form})
