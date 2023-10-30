from django.shortcuts import render
from .models import Product
from category.models import Category

# Create your views here.

def store(request):
    products = Product.objects.all().filter(is_available=True)
    categories = Category.objects.all()
    
    context = {
        'products' : products,
         'categories' : categories,
    }
        
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    return render(request, 'store/product_detail.html')