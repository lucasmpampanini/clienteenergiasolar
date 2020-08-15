from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')


def produtos_view(request):
    return render(request, 'produtos.html')