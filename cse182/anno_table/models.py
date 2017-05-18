from django.db import models

# Create your models here.
class Annotation(models.Model):
    """
        Annotation model
        Field corresponds to possible annotation sources, including comments
    """
    name = models.CharField(max_length=200, verbose_name='sequence_identifer')
    blast = models.CharField(max_length=200, verbose_name='blast_hit')
    pfam = models.CharField(max_length=200, verbose_name='pfam_hit')
    prosite = models.CharField(max_length=200, verbose_name='prosite_hit')
    kegg = models.CharField(max_length=200, verbose_name='kegg_pathway_hit')
    go = models.CharField(max_length=200, verbose_name='GO_hit')
    coment = models.CharField(max_length=200, verbose_name='comments')

    def __str__(self):
        return self.name
