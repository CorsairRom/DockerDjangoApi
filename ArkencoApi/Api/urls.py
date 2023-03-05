from django.urls import path
from ArkencoApi.Api.api import user_api_view, user_detail_view, client_api_view, client_detail_view, prospecto_api_view, prospecto_detail_view, ejemplo_api, LoginView, Login

urlpatterns = [
    path('usuario/', user_api_view, name='usuario_api'),
    path('usuario/<int:id>', user_detail_view, name='usuario_detail_api'),
    path('cliente/', client_api_view, name='cliente_api'),
    path('cliente/<str:rut>', client_detail_view, name='cliente_detail_api'),
    path('prospecto/', prospecto_api_view, name='prospecto_api'),
    path('prospecto/<str:cliente_id>', prospecto_detail_view, name='prospecto_detail_api'),
    path('ejemplo/', ejemplo_api.as_view(), name='prospecto_detail_api'),
    path('login/', Login.as_view(), name='login'),
]
 