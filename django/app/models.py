from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=30, null=True, blank=True)
    sobrenome = models.CharField(max_length=30, null=True, blank=True)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
