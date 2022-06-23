from django.db import models

class Renovacao(models.Model):

    dataDesocupacao = models.CharField(max_length=100)
    dataRenovacao = models.CharField(max_length=100)
    cartorio = models.CharField(max_length=100)

def __str__(self):
    return self.nome