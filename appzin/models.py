from django.db import models
#from django.contrib.auth.models import User
# Create your models here.

class Alunos(models.Model):
    id_aluno = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique = True)
    rg = models.CharField(max_length=8, unique = True)
    matricula = models.CharField(max_length=8)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=255)

class Professores(models.Model):
    id_professor = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique = True)
    rg = models.CharField(max_length=8, unique = True)
    codigo = models.CharField(max_length=8)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=11)

class Disciplinas(models.Model):
    id_disciplina = models.AutoField(primary_key = True)
    id_professor = models.ForeignKey(Professores, on_delete=models.SET_NULL)
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=7)
    carga_horaria = models.IntegerField()
    ementa = models.TextField(null = True, blank = True)

class DisciplinaAluno(models.Model):
    id_matricula = models.IntegerField(primary_key = True)
    id_aluno = models.ForeignKey(Alunos, on_delete=models.SET_NULL)
    id_disciplina = models.ForeignKey(Disciplinas, on_delete=models.SET_NULL)
    nota = models.FloatField(null = True, blank = True)
    
class PlanoAula(models.Model):
    id_plano_aula = models.AutoField(primary_key = True)
    id_disciplina = models.ForeignKey(Disciplinas, on_delete=models.SET_NULL)
    tema_aula = models.CharField(max_length=255)
    conteudo = models.TextField()
    metodo = models.CharField(max_length=50)
    dia = models.DateField()
 
class Atividades(models.Model):
    id_atividade = models.AutoField(primary_key = True)
    id_disciplina = models.ForeignKey(Disciplinas, on_delete=models.SET_NULL)
    id_plano_aula = models.ForeignKey(PlanoAula, on_delete=models.SET_NULL)
    atividade = models.TextField()
    tipo = models.CharField(max_length=50)
    data_postagem = models.DateField()
    data_entrega = models.DateField(null = True, blank = True)

class AtividadeAluno(models.Model):
    id = models.AutoField(primary_key = True)
    id_atividade = models.ForeignKey(Atividades, on_delete=models.SET_NULL)
    id_aluno = models.ForeignKey(Alunos, on_delete=models.SET_NULL)
    nota = models.FloatField(null = True, blank = True)

class Frequencia(models.Model):
    id_frequencia = models.AutoField(primary_key = True)
    id_materia = models.ForeignKey(Disciplinas, on_delete=models.SET_NULL)
    dia = models.DateField()

class FrequenciaAluno(models.Model):
    id = models.AutoField(primary_key = True)
    id_aluno = models.ForeignKey(Alunos, on_delete=models.SET_NULL)
    id_frequencia = models.ForeignKey(Frequencia, on_delete=models.SET_NULL)
    presenca = models.BooleanField()
