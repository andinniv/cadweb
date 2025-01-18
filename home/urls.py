from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('categoria/lista/',views.categoria, name="categoria"),
    path('categoria/formulario/',views.form_categoria, name="formulario"),
    path('categoria/formulario/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categoria/detalhes/<int:id>/', views.detalhes_categoria, name='detalhes_categoria'),
    path('categoria/remover/<int:id>/', views.remover_categoria, name='remover_categoria'),

######################################### CLIENTE ###############################################

    path('cliente/', views.cliente, name="cliente"),
    path('cliente/form_cliente/', views.form_cliente, name="form_cliente"),
    path('cliente/detalhes/<int:id>/', views.detalhes_cliente, name="detalhes_cliente"),
    path('editar_cliente/<int:id>/', views.editar_cliente, name="editar_cliente"),
    path('cliente/excluir/<int:id>/', views.excluir_cliente, name='excluir_cliente'),    


######################################### PRODUTO ################################################

    path('produto/', views.produto, name="produto"),
    path('produto/form_produto/', views.form_produto, name="form_produto"),
    path('produto/detalhes/<int:id>/', views.detalhes_produto, name="detalhes_produto"),
    path('produto/estoque/<int:id>/', views.ajustar_estoque, name="ajustar_estoque"),
    path('editar_produto/<int:id>/', views.editar_produto, name="editar_produto"),
    path('produto/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),
    path('ajustar_estoque/<int:id>', views.ajustar_estoque, name="ajustar_estoque"),
    ]