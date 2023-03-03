from rest_framework.viewsets import ModelViewSet
from ArkencoApi.models import Usuario, Cliente, Prospecto, Estado, Etapa
from ArkencoApi.Api.serializers import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    
