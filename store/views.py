from django.http import HttpResponse
from django.shortcuts import render

from .models import Plane


def index(request):
    # pylint: disable=fixme, no-member
    Planes = Plane.objects.all()
    data = {'planes' : Planes}
    return render(request, 'store/index.html', context=data)

def detail(request, plane_name):
    # pylint: disable=fixme, no-member
    data = {'plane' : Plane.objects.get(name=plane_name)}
    return render(request, 'store/detail.html', context=data)
