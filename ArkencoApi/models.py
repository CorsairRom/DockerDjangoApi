from django.db import models
# from django.contrib.auth.models import AbstractUser, Group, Permission, AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

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
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        # Encriptar el password antes de guardarlo
        self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Cliente(models.Model):
    nombre_empresa = models.CharField(max_length=200)
    rut = models.CharField(primary_key=True, max_length=12)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_empresa

class Estado(models.Model):
    estado = models.CharField(max_length=50)
    
    def __str__(self):
        return self.estado

class Etapa(models.Model):
    etapa = models.CharField(max_length=50)
    
    def __str__(self):
        return self.etapa
    
class Prospecto(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.IntegerField()
    fecha_ingreso = models.DateField()
    sexo = models.CharField(max_length=20)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estado_id = models.ForeignKey(Estado, on_delete=models.CASCADE)
    estapa_id = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    
#-----------------------


