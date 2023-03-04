from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from django.http import HttpResponse
from .models import Usuario, Cliente, Prospecto, Estado, Etapa


class ClienteView(View):
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
        pass
    
    def put(self, request):
        pass
    
    def delete(self, request):
        pass
    