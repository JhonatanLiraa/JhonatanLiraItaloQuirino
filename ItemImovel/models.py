from django.db import models

class ItemImovel(models.Model):

    Fotos = models.CharField(max_length=100)

def __str__(self):
    return self.nome