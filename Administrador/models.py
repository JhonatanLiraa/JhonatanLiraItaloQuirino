from django.db import models

class Administrador(models.Model):

    calcular_Salario = models.CharField(max_length=100)

def __str__(self):
    return self.nome