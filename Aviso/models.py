from django.db import models

class Aviso(models.Model):

    matricula_avi = models.CharField(max_length=100)
    assunto_avi = models.CharField(max_length=100)
    data_avi = models.CharField(max_length=100)

def __str__(self):
    return self.nome