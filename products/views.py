from django.shortcuts import render
from .models import Product, Category

def products_view(request):
    context = {
        'categorys': Category.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, "produtos.html", context)


def products_details(request, slug, pk):
    context = {
        'product': Product.objects.get(id=pk)
    }
    return render(request, "product_details.html", context)


def products_filter(request, pk):
    context = {
        'categorys': Category.objects.all(),
        'products': Product.objects.filter(category=pk),
        'category': Category.objects.get(id=pk),
    }
    return render(request, "produtos.html", context)