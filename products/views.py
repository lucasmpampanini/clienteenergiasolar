from django.shortcuts import render
from .models import Product

def products_view(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, "produtos.html", context)


def products_details(request, slug, pk):
    context = {
        'product': Product.objects.get(id=pk)
    }
    return render(request, "product_details.html", context)