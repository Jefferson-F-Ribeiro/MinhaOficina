from django.contrib.auth.models import AbstractUser
from django.db import models

class Oficina(AbstractUser):
    # Campos adicionais específicos da oficina
    nome_oficina = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='oficina_set',
        related_query_name='oficina',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='oficina_set',
        related_query_name='oficina',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        )

    def __str__(self):
        return self.username

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE, related_name='clientes')

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='veiculos')

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.ano})'

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='servicos')

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    servicos = models.ManyToManyField(Servico)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido #{self.id} - {self.cliente}'
