from django.urls import path
from .views import ClienteView, UsuarioView
from . import views

urlpatterns = [
    
    path('cliente/', ClienteView.as_view(), name='cliente'),
    path('cliente/<int:id>', ClienteView.as_view(), name='cliente_id'),
    path('usuario/', UsuarioView.as_view(), name='usuario'),
    path('usuario/<int:id>', UsuarioView.as_view(), name='usuario_id'),
]