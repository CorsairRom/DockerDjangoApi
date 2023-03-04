from django.urls import path
from .views import ClienteView
from . import views

urlpatterns = [
    
    path('cliente/', ClienteView.as_view(), name='cliente'),
]