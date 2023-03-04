from rest_framework.serializers import ModelSerializer
from ArkencoApi.models import Usuario, Cliente, Prospecto, Estado, Etapa

class UsuarioSerializer(ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = '__all__'
        
class ClienteSerializer(ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = '__all__'
        
class ProspectoSerializer(ModelSerializer):
    
    class Meta:
        model = Prospecto
        fields = '__all__'
        
class EstadoSerializer(ModelSerializer):
    
    class Meta:
        model = Estado
        fields = '__all__'
        
class EtapaSerializer(ModelSerializer):
    
    class Meta:
        model = Etapa
        fields = '__all__'
