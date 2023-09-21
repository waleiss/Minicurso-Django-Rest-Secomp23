from rest_framework import viewsets
from .models import *
from .serializers import *

#from rest_framework.decorators import action
#from rest_framework.response import Response
#   @action(detail=True, method=["get"])
#   def data_modelo(self, request, pk=None):

class AlunosViews(viewsets.ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer

class ProfessoresViews(viewsets.ModelViewSet):
    queryset = Professores.objects.all()
    serializer_class = ProfessoresSerializer

class DisciplinasViews(viewsets.ModelViewSet):
    queryset = Disciplinas.objects.all()
    serializer_class = DisciplinasSerializer

class DisciplinaAlunoViews(viewsets.ModelViewSet):
    queryset = DisciplinaAluno.objects.all()
    serializer_class = DisciplinaAlunoSerializer

class PlanoAulaViews(viewsets.ModelViewSet):
    queryset = PlanoAula.objects.all()
    serializer_class = PlanoAulaSerializer

class AtividadesViews(viewsets.ModelViewSet):
    queryset = Atividades.objects.all()
    serializer_class = AtividadesSerializer

class AtividadeAlunoViews(viewsets.ModelViewSet):
    queryset = AtividadeAluno.objects.all()
    serializer_class = AtividadeAlunoSerializer

class FrequenciaViews(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer

class FrequenciaAlunoViews(viewsets.ModelViewSet):
    queryset = FrequenciaAluno.objects.all()
    serializer_class = FrequenciaAlunoSerializer