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
    path('remover_cliente/<int:id>/', views.remover_cliente, name='remover_cliente'),    


######################################### PRODUTO ################################################

    path('produto/', views.produto, name="produto"),
    path('produto/form_produto/', views.form_produto, name="form_produto"),
    path('produto/detalhes/<int:id>/', views.detalhes_produto, name="detalhes_produto"),
    path('produto/estoque/<int:id>/', views.ajustar_estoque, name="ajustar_estoque"),
    path('editar_produto/<int:id>/', views.editar_produto, name="editar_produto"),
    path('produto/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),
    path('ajustar_estoque/<int:id>', views.ajustar_estoque, name="ajustar_estoque"),

################################ TESTE #######################################################

    path('teste1/', views.teste1, name='teste1'),
    path('teste2/', views.teste2, name='teste2'),
    path('buscar_dados/<str:app_modelo>/', views.buscar_dados, name='buscar_dados'),
    path('teste3/', views.teste3, name='teste3'),

###################################### PEDIDO #####################################################
    path('pedido/', views.pedido, name='pedido'),
    path('pedido/novo_pedido/<int:id>', views.novo_pedido, name='novo_pedido'),
    path('pedido/detalhes/<int:id>/', views.detalhes_pedido, name='detalhes_pedido'),
    path('editar_pedido/<int:id>/', views.editar_pedido, name='editar_pedido'),
    path('remover_pedido/<int:id>/', views.remover_pedido, name='remover_pedido'),
    path('remover_item_pedido/<int:id>/', views.remover_item_pedido, name='remover_item_pedido'),
    path('editar_item_pedido/<int:id>/', views.editar_item_pedido, name='editar_item_pedido'),
    path('form_pagamento/<int:id>/', views.form_pagamento, name='form_pagamento'),
    path('remover_pagamento/<int:id>/', views.remover_pagamento, name='remover_pagamento'),
    path('notafiscal/<int:pedido_id>/', views.notafiscal, name='notafiscal'),


    ]