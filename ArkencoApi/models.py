from django.db import models

#--------Opciones-----
estado = [
    ('Abierto', 'Abierto'),
    ('Perdido', 'Perdido'),
    ('Ganado', 'Ganado'),
]

etapa = [
    ('En conversacion', 'En conversacion'),
    ('Conseguido', 'Conseguido'),
    ('Perdido', 'Perdido'),
]

#----------------------

#---------Models-------

class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

class Cliente(models.Model):
    nombre_empresa = models.CharField(max_length=200)
    rut = models.CharField(primary_key=True, max_length=12)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
class Estado(models.Model):
    estado = models.CharField(choices=estado)

class Etapa(models.Model):
    etapa = models.CharField(choices=etapa)
    
    
#-----------------------


