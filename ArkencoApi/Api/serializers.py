from rest_framework.serializers import ModelSerializer
from ArkencoApi.models import Usuario, Cliente, Prospecto, Estado, Etapa

class UsuarioSerializer(ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = '__all__'