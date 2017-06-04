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
    #file_path = os.path.join(settings.MEDIA_ROOT, '../../../../ANNOTATIONS/data.csv')
    file_path = os.path.join(settings.MEDIA_ROOT, '')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
