from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import redirect
from django.contrib import messages

from .models import MakeupProduct
from .forms import MakeupProductForm

# View for listing products

def home(request):
    return render(request, 'home.html')

def product_list(request):
    products = MakeupProduct.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# View for creating a product
def product_create(request):
    if request.method == "POST":
        form = MakeupProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = MakeupProductForm()
    return render(request, 'products/product_form.html', {'form': form})

# View for updating a product
def product_update(request, pk):
    product = get_object_or_404(MakeupProduct, pk=pk)
    if request.method == "POST":
        form = MakeupProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = MakeupProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})


def product_delete(request, pk):
    try:
        product = MakeupProduct.objects.get(pk=pk)
        if request.method == "POST":
            product.delete()
            messages.success(request, "Product deleted successfully.")
            return redirect('product_list')
        return render(request, 'products/product_confirm_delete.html', {'product': product})
    except MakeupProduct.DoesNotExist:
        messages.error(request, "Product does not exist.")
        return redirect('product_list')

