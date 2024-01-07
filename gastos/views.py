from django.shortcuts import render
from .models import Gasto
from django.db.models import Q
from django.http import JsonResponse
from utils.validators import *
from django.db.models import Max

# Create your views here.
def gastos_form(request):
     id = request.GET.get('id')
     return render(request,"gastos_form.html",{'id':id})

def grupo_atual():
    max_grupo = Gasto.objects.all().aggregate(Max('grupo'))['grupo__max']
    return max_grupo if max_grupo is not None else 1

def gastos_salva(request):
        obs = request.POST.get('obs')
        if Validator.empty(obs):
          data={'success':False, 'message':'Preencha o campo OBS'}
          return JsonResponse(data)

        valor = request.POST.get('valor')
        if not Validator.positive(valor):
          data={'success':False, 'message':'O valor precisa ser maior do que zero'}
          return JsonResponse(data)

        obj_gastos = Gasto()
        obj_gastos.obs = obs
        obj_gastos.valor = valor
        obj_gastos.grupo = grupo_atual()
        obj_gastos.fk_categorias_id = request.POST.get('fk_categorias')
        obj_gastos.save()
        data={'success':True, 'message':'Sucesso ao salvar a transação'+ request.POST.get('fk_categorias')}
        return JsonResponse(data)

def gastos_lista(request):
   id_categoria = request.GET.get('id')
   grupo = grupo_atual()
   obj_gastos = Gasto.objects.filter(fk_categorias_id = id_categoria, grupo=grupo).values().order_by('date_add')

   return render(request,"gastos_lista.html",{'obj_gastos': obj_gastos})

def gastos_del(request):
    id = request.GET.get('id')
    obj_gastos = Gasto(id=id)
    obj_gastos.delete()
    return JsonResponse({'success':True, 'message':'Gasto apagado'})

def gastos_reinicia(request):
    obj_gastos = Gasto()
    grupo = grupo_atual()
    grupo_novo = grupo + 1
    obj_gastos.obs = 'reiniciou'
    obj_gastos.valor = 0
    obj_gastos.grupo = grupo_novo
    obj_gastos.fk_categorias_id = 1
    obj_gastos.save()
    return JsonResponse({'success':True, 'message':'Reiniciado'})

