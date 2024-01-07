from django.urls import path
from . import views

urlpatterns = [
      path('', views.categorias_index),
      path('form/', views.categorias_form,name='categorias_form'),
      path('form/salvar/', views.categorias_salva,name='categorias_salvar'),
      path('list/', views.categorias_lista,name='categorias_listar'),
      path('list/del/', views.categorias_del, name='categorias_del'),
      path('list/edit/', views.categorias_edit, name='categorias_edit')

]
