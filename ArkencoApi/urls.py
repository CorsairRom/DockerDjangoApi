from django.urls import path
from .views import  UsuarioView
from . import views

urlpatterns = [
    
    path('usuario/', UsuarioView.as_view(), name='usuario'),
    path('usuario/<int:id>', UsuarioView.as_view(), name='usuario_id'),
]