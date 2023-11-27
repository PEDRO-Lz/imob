from django.db import models
from django.contrib.auth.models import User

class Proprietario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self):
        return self.usuario.username

    def propriedades(self):
        return self.imoveis_possuidos.all()

class Locatario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)

    def alugando(self):
        return self.imovel_locado
class Imovel(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=5)
    preco = models.IntegerField()
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE, related_name='imoveis_possuidos')
    locatario = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='imovel_locado_locatario')
