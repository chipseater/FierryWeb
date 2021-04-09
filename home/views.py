from django.shortcuts import render
from . import templates

def Index(request):
    return render(request, 'home/index.html')
