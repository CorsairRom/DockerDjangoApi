from rest_framework.viewsets import ModelViewSet
from ArkencoApi.models import Usuario, Cliente, Prospecto, Estado, Etapa
from ArkencoApi.Api.serializers import UsuarioSerializer, ClienteSerializer, ProspectoSerializer, EstadoSerializer, EtapaSerializer

class UsuarioViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    
class ClienteViewSet(ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    
class ProspectoViewSet(ModelViewSet):
    serializer_class = ProspectoSerializer
    queryset = Prospecto.objects.all()
    
class EstadoViewSet(ModelViewSet):
    serializer_class = EstadoSerializer
    queryset = Estado.objects.all()
    
class EtapaViewSet(ModelViewSet):
    serializer_class = EtapaSerializer
    queryset = Etapa.objects.all()
    
