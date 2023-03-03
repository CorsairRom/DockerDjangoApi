from rest_framework.routers import DefaultRouter
from ArkencoApi.Api.views import UsuarioViewSet

router_posts = DefaultRouter()

router_posts.register(prefix='post', basename='post', viewset=UsuarioViewSet)