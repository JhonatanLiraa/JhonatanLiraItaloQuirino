from django.db import models

class Agendamento(models.Model):

    dia = models.CharField(max_length=100)
    hora = models.CharField(max_length=100)
    local = models.CharField(max_length=100)

def __str__(self):
    return self.nome