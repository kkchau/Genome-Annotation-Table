import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404
from .models import Annotation

# Create your views here.

def base(request):
    """
        Base view
        Simply gathers annotations and collects that set and the template into
            the context
        Also reads the stats file
    """
    annotations = Annotation.objects.all()

    # stats dictionary
    statistics = {
        'name': 0, 
        'blast': 0, 
        'pfam': 0, 
        'prosite': 0, 
        'kegg': 0, 
        'go': 0, 
        'coment': 0
    }

    # calculate statistics
    for annotation in annotations:
        fields = ['name', 'blast', 'pfam', 'prosite', 'kegg', 'go', 'coment']
        for key in fields:
            if getattr(annotation, key):
                statistics[key] += 1

    max_count = statistics['name']
    for field in statistics:
        statistics[field] = statistics[field] / max_count

    return render(request, 'anno_table/base.html', {
        'annotations': annotations, 'statistics': statistics
    })


def download(request):
    """
        Be able to download the data.csv file
    """
    with open('ANNOTATIONS/data.csv') as downFile:
        response = HttpResponse(downFile.read())
        response['content_type'] = 'text/csv'
        response['Content-Disposition'] = 'attachment;filename=data.csv'
    return response


def raw_disp(request, filename):
    """
        Display raw alignment file for the given filename
    """
    with open('ANNOTATIONS/raw_aligns/{}.txt'.format(filename), 'r') as raw:
        align = raw.readlines() 
    return render(
        request, 'anno_table/raw.html', {'filename': filename, 'alignment': align}
    )
