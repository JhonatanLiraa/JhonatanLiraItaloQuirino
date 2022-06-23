from django.db import models

class Corretor(models.Model):

    comissao = models.CharField(max_length=100)
    idCorretor = models.CharField(max_length=100)

def __str__(self):
    return self.nome