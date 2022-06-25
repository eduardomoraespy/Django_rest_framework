from tabnanny import verbose
from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50, verbose_name='nome')
    endereco = models.CharField(max_length=50, verbose_name='endereço')
    idade = models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        db_table = 'cliente'

