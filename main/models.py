from django.db import models

# Create your models here.

class Produtos(models.Model):
    produto_id = models.AutoField(primary_key= True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    
    def __str__(self):
        return self.nome
    