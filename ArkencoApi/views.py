from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Usuario, Cliente, Prospecto, Estado, Etapa


class ClienteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        clientes = list(Cliente.objects.values())
        if len(clientes) > 0:
            datos = {
                'message': 'Success',
                'Clientes' : clientes
            }
        else:
            datos = { 'message': "No Data Found..."}
        return JsonResponse(datos)

    def post(self, request):
        jsonData =  json.loads(request.body)
        
        datos = { 'message': "No Data Found..."}
        return JsonResponse(datos)
    
    def put(self, request):
        pass
    
    def delete(self, request):
        pass
    
class UsuarioView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id>0):
            usuarios = list(Usuario.objects.filter(id = id).values())
            if len(usuarios)>0:
                usuario = usuarios[0]
                datos = { 'message': "success", 'usuario': usuario}
            else:
                datos = { 'message': "User Not Found..."}
            return JsonResponse(datos)
        else:
            usuarios = list(Usuario.objects.values())
            if len(usuarios) > 0:
                datos = {
                    'message': 'Success',
                    'Clientes' : usuarios
                }
            else:
                datos = { 'message': "No Data Found..."}
            return JsonResponse(datos)

    def post(self, request):
        jsonData =  json.loads(request.body)
        #print(jsonData)
        try:
            Usuario.objects.create(username=jsonData['username'], password=jsonData['password'])
            datos = { 'message': "Success"}
        except:
            datos = { 'message': "Incorrect Data"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jsonData =  json.loads(request.body)
        usuarios = list(Usuario.objects.filter(id = id).values())
        if len(usuarios)>0:
            user = Usuario.objects.get(id=id)
            user.username = jsonData['username']
            user.password = jsonData['password']
            user.save()
            datos = { 'message': f"Update User {id} Success"}
        else:
            datos = { 'message': f"User {id} not found"}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        usuarios = list(Usuario.objects.filter(id = id).values())
        if len(usuarios)>0:
            user = Usuario.objects.get(id = id)
            user.delete()
            datos = {'message' : f"User {id} delete"}
        else:
            datos = { 'message' : f"User {id} not found"}
        return JsonResponse(datos)
    