from rest_framework.routers import DefaultRouter
from ArkencoApi.Api.views import UsuarioViewSet, ClienteViewSet, ProspectoViewSet, EstadoViewSet, EtapaViewSet

router_posts = DefaultRouter()

router_posts.register(prefix='user', basename='user', viewset=UsuarioViewSet)
router_posts.register(prefix='client', basename='client', viewset=ClienteViewSet)
router_posts.register(prefix='prospecto', basename='prospecto', viewset=ProspectoViewSet) #falta filtrar por cliente
router_posts.register(prefix='estado', basename='estado', viewset=EstadoViewSet) 
router_posts.register(prefix='etapa', basename='etapa', viewset=EtapaViewSet) 
