from django.db import models
#from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField(null = True, blank = True, max_length=30)
    first_name = models.CharField(null = True, blank = True, max_length=30)
    last_name = models.CharField(null = True, blank = True, max_length=30)

class Contas(models.Model):
    id_conta = models.AutoField(primary_key = True)
    tp_conta = models.CharField(max_length=30)
    id_banco = models.IntegerField()
    banco = models.CharField(max_length=50)
    conta = models.IntegerField()
    agencia = models.IntegerField()
    operacao = models.IntegerField()

class Ufs(models.Model):
    id_uf = models.AutoField(primary_key = True)
    nome_uf = models.CharField(max_length=30)
    sigla_uf = models.CharField(max_length=2) 

class Cidades(models.Model):
    id_cidade = models.IntegerField(primary_key = True)
    nome_cidade = models.CharField(max_length=50)
    id_uf = models.ForeignKey(Ufs, on_delete=models.CASCADE)

class Enderecos(models.Model):
    id_endereco = models.IntegerField(primary_key = True)
    id_cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=8)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=80)
    complemento = models.CharField(max_length=60, null = True, blank = True)
    observacoes = models.TextField(null = True, blank = True)

class Pessoas(models.Model):

    id_pessoa = models.AutoField(primary_key = True)
    vinculo = models.CharField(max_length=20)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    cpf = models.IntegerField(unique = True)
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=16)
    email = models.EmailField()
    id_endereco = models.IntegerField()
    id_conta = models.ForeignKey(Contas, on_delete=models.CASCADE)

class Ocorrencias(models.Model):
    id_ocorrencia = models.AutoField(primary_key = True)
    data = models.DateField() #auto_now_add=True
    realizada = models.CharField(max_length=1)
    ocorrencia = models.TextField()
    id_pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
