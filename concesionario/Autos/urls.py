from django.urls import path

from .import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('listado_Autos', views.Autos, name='autos'),
    path('listado_clientes', views.clientes, name='clientes'),
]