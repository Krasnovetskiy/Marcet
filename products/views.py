from django.shortcuts import render

def products(request, *args, **kwargs):
    return render(request, 'app products/index.html')
