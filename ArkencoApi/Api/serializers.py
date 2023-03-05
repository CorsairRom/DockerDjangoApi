from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ArkencoApi.models import Usuario, Cliente, Prospecto, Estado, Etapa
from ArkencoApi.Rut import validarRut
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class UsuarioSerializer(ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = '__all__'
        
        
class ClienteSerializer(ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def validate_rut(self, value):
        rut = value
        if validarRut(str(rut)) == False:
            raise serializers.ValidationError("Rut inválido")
        return value
        
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
