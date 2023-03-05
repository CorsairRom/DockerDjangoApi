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


#Opcion para Crear usuario Custome
# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('El usuario debe tener un nombre de usuario válido')

#         user = self.model(
#             username=username,
#             **extra_fields
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(
#             username=username,
#             password=password,
#             **extra_fields
#         )

# class Usuario(AbstractBaseUser):
#     username = models.CharField(max_length=30, unique=True)
#     password = models.CharField(max_length=128)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'username'

#     def __str__(self):
#         return self.username



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


