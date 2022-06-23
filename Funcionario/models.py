from django.db import models

class Funcionario(models.Model):

    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    dataNascimento = models.CharField(max_length=100)
    carteiraTrabalho = models.CharField(max_length=100)
    salario = models.CharField(max_length=100)
    pis = models.CharField(max_length=100)

def __str__(self):
    return self.nome