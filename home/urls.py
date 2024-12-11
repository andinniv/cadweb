from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('categoria/lista/',views.categoria, name="categoria"),
    path('categoria/formulario/',views.form_categoria, name="formulario"),
    
]