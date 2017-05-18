from django.shortcuts import render
from django.http import HttpResponse
from .models import Annotation

# Create your views here.

def base(request):
    annotations = Annotation.objects.all()
    return render(request, 'anno_table/base.html', {'annotations': annotations)
