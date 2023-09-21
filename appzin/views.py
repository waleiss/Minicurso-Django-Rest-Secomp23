from rest_framework import viewsets
from .models import *
from .serializers import *

#from rest_framework.decorators import action
#from rest_framework.response import Response
#   @action(detail=True, method=["get"])
#   def data_modelo(self, request, pk=None):

class UserViews(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ContasViews(viewsets.ModelViewSet):
    queryset = Contas.objects.all()
    serializer_class = ContasSerializer

class UfsViews(viewsets.ModelViewSet):
    queryset = Ufs.objects.all()
    serializer_class = UfsSerializer

class CidadesViews(viewsets.ModelViewSet):
    queryset = Cidades.objects.all()
    serializer_class = CidadesSerializer

class EnderecosViews(viewsets.ModelViewSet):
    queryset = Enderecos.objects.all()
    serializer_class = EnderecosSerializer

class PessoasViews(viewsets.ModelViewSet):
    queryset = Pessoas.objects.all()
    serializer_class = PessoasSerializer

class OcorrenciasViews(viewsets.ModelViewSet):
    queryset = Ocorrencias.objects.all()
    serializer_class = OcorrenciasSerializer