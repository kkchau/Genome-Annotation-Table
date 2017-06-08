import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404
from .models import Annotation


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
        'Sequence': 0, 
        'BLAST': 0, 
        'Pfam': 0, 
        'Prosite': 0, 
        'KEGG_Pathway': 0, 
        'NucPloc': 0,
        'Gene_Ontology': 0, 
        'Comments': 0
    }

    # get statistics
    with open('ANNOTATIONS/statistics.tsv') as stats_in:
        for line in stats_in:
            line = line.strip().split('\t')
            line[0] = '_'.join(line[0].strip().split())
            statistics[line[0]] = float(line[1]) / float(line[2])

    return render(request, 'anno_table/base.html', {
        'annotations': annotations, 'statistics': statistics
    })


def download(request):
    """
        Be able to download the data.csv file
    """
    with open('ANNOTATIONS/data_full.csv') as downFile:
        response = HttpResponse(downFile.read())
        response['content_type'] = 'text/csv'
        response['Content-Disposition'] = 'attachment;filename=data.csv'
    return response


def raw_disp(request, filename):
    """
        Display raw alignment file for the given filename
    """
    raw_annotations = {
        'BLAST': ['No Annotation'], 
        'Pfam': ['No Annotation'], 
        'Prosite': ['No Annotation'], 
        'KEGG': ['No Annotation'], 
        'NucPloc': ['No Annotation'],
        'GO': ['No Annotation']
    }
    for a in raw_annotations:
        file_path = 'ANNOTATIONS/raw_aligns/{}/{}.txt'.format(a, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as raw:
                raw_annotations[a] = raw.readlines() 
    raw_annotations['filename'] = filename
    return render(request, 'anno_table/raw.html', raw_annotations)
