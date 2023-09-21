from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
   class Meta: 
        model = User
        fields = '__all__'

class ContasSerializer(serializers.ModelSerializer):
   class Meta: 
        model = Contas
        fields = '__all__'

class UfsSerializer(serializers.ModelSerializer):
   class Meta: 
        model = Ufs
        fields = '__all__'  

class CidadesSerializer(serializers.ModelSerializer):
   class Meta: 
        model = Cidades
        fields = '__all__'

class EnderecosSerializer(serializers.ModelSerializer):
   class Meta: 
        model = Enderecos
        fields = '__all__'

class PessoasSerializer(serializers.ModelSerializer):
   class Meta: 
        model = Pessoas
        fields = '__all__'

class OcorrenciasSerializer(serializers.ModelSerializer):
   class Meta: 
        model = Ocorrencias
        fields = '__all__'