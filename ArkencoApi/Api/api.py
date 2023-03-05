from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ArkencoApi.Api.serializers import UsuarioSerializer, ClienteSerializer, EstadoSerializer, EtapaSerializer, ProspectoSerializer
from ArkencoApi.models import Cliente, Estado, Etapa, Prospecto, Usuario



# ------------------User Api---------------
@api_view(['GET', 'POST'])
def user_api_view(request):
    #list user
    if request.method == 'GET':
        user = Usuario.objects.all()
        user_serializer = UsuarioSerializer(user, many=True)
        return Response(user_serializer.data , status=status.HTTP_200_OK)
    #create user
    elif request.method == 'POST':
        user_serializer = UsuarioSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request, id):
    #queryset user
    user = Usuario.objects.filter(id = id).first()
    
    #validate user
    if user:
        # retive user
        if request.method == 'GET':
            user_serializer = UsuarioSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        # update user
        elif request.method == 'PUT':
            user_serializer = UsuarioSerializer(user, data=request.data )
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # delelte user
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message': f'User id:{id} deleted'}, status=status.HTTP_200_OK)
    
    return Response({'message': f"User id:{id} not found"}, status=status.HTTP_400_BAD_REQUEST)


# ------------------Client Api---------------
@api_view(['GET', 'POST'])
def client_api_view(request):
    #list client
    if request.method == 'GET':
        client = Cliente.objects.all()
        client_serializer = ClienteSerializer(client, many=True)
        return Response(client_serializer.data , status=status.HTTP_200_OK)
    #create client
    elif request.method == 'POST':
        client_serializer = ClienteSerializer(data=request.data)
        if client_serializer.is_valid():
            client_serializer.save()
            return Response(client_serializer.data, status=status.HTTP_201_CREATED)
        return Response(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def client_detail_view(request,rut):
    #queryset client
    client = Cliente.objects.filter(rut = rut).first()
    
    #validate client
    if client:
        # retive client
        if request.method == 'GET':
            client_serializer = ClienteSerializer(client)
            return Response(client_serializer.data, status=status.HTTP_200_OK)
        # update client
        elif request.method == 'PUT':
            client_serializer = ClienteSerializer(client, data=request.data )
            if client_serializer.is_valid():
                client_serializer.save()
                return Response(client_serializer.data, status=status.HTTP_200_OK)
            return Response(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # delelte client
        elif request.method == 'DELETE':
            client.delete()
            return Response({'message': f'Client Rut:{rut} deleted'}, status=status.HTTP_200_OK)
    
    return Response({'message': f"Client Rut:{rut} not found"}, status=status.HTTP_400_BAD_REQUEST)

# ------------------Prospecto Api---------------

@api_view(['GET', 'POST'])
def prospecto_api_view(request):
    #list prospecto
    if request.method == 'GET':
        prospecto = Prospecto.objects.all()
        prospecto_serializer = ProspectoSerializer(prospecto, many=True)
        return Response(prospecto_serializer.data , status=status.HTTP_200_OK)
    #create prospecto
    elif request.method == 'POST':
        prospecto_serializer = ProspectoSerializer(data=request.data)
        if prospecto_serializer.is_valid():
            prospecto_serializer.save()
            return Response(prospecto_serializer.data, status=status.HTTP_201_CREATED)
        return Response(prospecto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def prospecto_detail_view(request,cliente_id):
    #queryset prospecto
    prospecto = Prospecto.objects.filter(cliente_id = cliente_id).first()
    #validate prospecto
    if prospecto:
        # obtain name prospect
        name = prospecto.nombre
        # retive prospecto
        if request.method == 'GET':
            prospecto_serializer = ProspectoSerializer(prospecto)
            return Response(prospecto_serializer.data, status=status.HTTP_200_OK)
        # update prospecto
        elif request.method == 'PUT':
            prospecto_serializer = ProspectoSerializer(prospecto, data=request.data )
            if prospecto_serializer.is_valid():
                prospecto_serializer.save()
                return Response(prospecto_serializer.data, status=status.HTTP_200_OK)
            return Response(prospecto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # delelte prospecto
        elif request.method == 'DELETE':
            prospecto.delete()
            return Response({'message': f'Prospecto Name:{name} deleted'}, status=status.HTTP_200_OK)
    
    return Response({'message': f"Client ID:{cliente_id} not have Prospectos"}, status=status.HTTP_400_BAD_REQUEST)

# ------------------Estado Api---------------
@api_view(['GET'])
def estado_api_view(request):
    #list estado
    if request.method == 'GET':
        estado = Estado.objects.all()
        estado_serializer = EstadoSerializer(estado, many=True)
        return Response(estado_serializer.data , status=status.HTTP_200_OK)
    
# ------------------Etapa Api---------------
@api_view(['GET'])
def etapa_api_view(request):
    #list etapa
    if request.method == 'GET':
        etapa = Etapa.objects.all()
        etapa_serializer = EtapaSerializer(etapa, many=True)
        return Response(etapa_serializer.data , status=status.HTTP_200_OK)