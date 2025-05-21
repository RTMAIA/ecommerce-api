from django.db import models


# Create your models here.
class Produtos(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    quantidade_estoque = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome