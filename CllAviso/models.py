from django.db import models

class CllAviso(models.Model):

    mensagem = models.CharField(max_length=100)

def __str__(self):
    return self.nome