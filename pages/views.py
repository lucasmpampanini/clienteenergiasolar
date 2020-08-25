from django.shortcuts import render
from services.models import Service

def index_view(request):
    context = {
        'services': Service.objects.all()
    }
    return render(request, 'index.html', context)

def service_details(request, slug, pk):
    context = {
        'service': Service.objects.get(id=pk)
    }
    return render(request, "service_details.html", context)
