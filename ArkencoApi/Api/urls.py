from django.urls import path
from ArkencoApi.Api.api import user_api_view, user_detail_view, client_api_view, client_detail_view, prospecto_api_view, prospecto_detail_view, Login, estado_api_view, etapa_api_view

urlpatterns = [
    path('usuario/', user_api_view, name='usuario_api'),
    path('usuario/<int:id>', user_detail_view, name='usuario_detail_api'),
    path('cliente/', client_api_view, name='cliente_api'),
    path('cliente/<str:rut>', client_detail_view, name='cliente_detail_api'),
    path('prospecto/', prospecto_api_view, name='prospecto_api'),
    path('prospecto/<str:cliente_id>', prospecto_detail_view, name='prospecto_detail_api'),
    path('login/', Login.as_view(), name='login'),
    path('estado/', estado_api_view, name='estado_api'),
    path('etapa/', etapa_api_view, name='etapa_api'),
]
 