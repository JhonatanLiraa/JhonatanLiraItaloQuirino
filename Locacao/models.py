from django.db import models

class Locacao(models.Model):

    dataDesocupacao = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    formaGarantia = models.CharField(max_length=100)
    fiador = models.CharField(max_length=100)

def __str__(self):
    return self.nome