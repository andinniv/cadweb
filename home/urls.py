from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('categoria/lista/',views.categoria, name="categoria"),
    path('categoria/formulario/',views.form_categoria, name="formulario"),
    path('categoria/formulario/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categoria/detalhes/<int:id>/', views.detalhes_categoria, name='detalhes_categoria'),
    path('categoria/remover/<int:id>/', views.remover_categoria, name='remover_categoria'),

    path('cliente/', views.cliente, name="cliente"),
    path('cliente/form_cliente/', views.form_cliente, name="form_cliente"),
    path('cliente/detalhes/<int:id>/', views.detalhes_cliente, name="detalhes_cliente"),
    path('editar_cliente/<int:id>/', views.editar_cliente, name="editar_cliente"),
    path('cliente/excluir/<int:id>/', views.excluir_cliente, name='excluir_cliente'),    
]