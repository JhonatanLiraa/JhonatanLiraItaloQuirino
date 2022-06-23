from django.db import models

class Gerente(models.Model):

    comissao = models.CharField(max_length=100)
    
def __str__(self):
    return self.nome