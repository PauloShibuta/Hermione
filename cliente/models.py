from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=300)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=300)
    telefone = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
