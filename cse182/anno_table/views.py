from django.shortcuts import render
from django.http import HttpResponse
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
