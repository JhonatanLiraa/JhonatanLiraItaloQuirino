from django.db import models

class Cheque(models.Model):

    financeiro = models.CharField(max_length=100)
    nomeCliente = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    dataAbertura = models.CharField(max_length=100)

def __str__(self):
    return self.nome