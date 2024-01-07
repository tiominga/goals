from django.urls import path
from . import views

urlpatterns = [
      #path('', views.gastos_index),
      path('form/', views.gastos_form,name='gastos_form'),
      path('form/salvar/', views.gastos_salva,name='gastos_salvar'),
      path('list/', views.gastos_lista,name='gastos_listar'),
      path('list/del/', views.gastos_del, name='gastos_del'),
      path('reinicia/',views.gastos_reinicia,name='gastos_reinicia')
      #path('list/edit/', views.gastos_edit, name='gastos_edit')

]
