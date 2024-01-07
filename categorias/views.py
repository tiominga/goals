from django.shortcuts import render
from .models import Categoria
from gastos.models import Gasto
from gastos.views import grupo_atual
from django.http import JsonResponse
from django.db import IntegrityError
from django.db.models import Q,Sum
from utils.validators import Validator

def categorias_index(request):
    return render(request,"categorias_index.html")

def categorias_form(request):
    return render(request,"categorias_form.html")

def categorias_salva(request):

    id = request.POST.get('id')

    if id == '': #inserindo
        obj_categoria = Categoria()
    else: #editando
        obj_categoria =  Categoria.objects.get(id=id)

    obj_categoria.nome = request.POST.get('nome')
    obj_categoria.meta = request.POST.get('meta')

    if  Validator.empty(obj_categoria.nome):
        data = {'success':'false','message':'O nome precisa ser preenchido'}
        return JsonResponse(data)

    if not Validator.positive(obj_categoria.meta):
        data = {'success':'false','message':'O valor da meta precisa ser maior do que zero'}
        return JsonResponse(data)

    try:
        obj_categoria.save()
        data = {'success':'true','message':'Salvo com sucesso...'}
    except IntegrityError:
        data = {'success':'false','message':'Erro, reveja os campos'}

    return JsonResponse(data)

def limite_gastos(id_categoria):
    print('procurarei poir',id_categoria)
    obj_categoria = Categoria.objects.filter(id=id_categoria).values('meta','nome').order_by('nome').first()
    return obj_categoria['meta']

def resta(id_categoria):
    grupo = grupo_atual()
    jagasto = total_gastos(id_categoria)
    limite = limite_gastos(id_categoria)
    resta = limite - jagasto
    resta = round(resta,2)
    return resta

def total_gastos(id_categoria):
    grupo = grupo_atual()
    total = Gasto.objects.filter(fk_categorias_id=id_categoria, grupo=grupo).aggregate(Sum('valor'))['valor__sum'] or 0
    total = round(total,2)
    return total

def percentual(id_categoria):
    grupo = grupo_atual()
    limite = limite_gastos(id_categoria)
    total = total_gastos(id_categoria)
    perc = round((total * 100)/limite,2)
    perc_str = str(perc).replace(',', '.')
    return perc_str

def categorias_lista(request):
    valor = request.POST.get('valor')

    if valor is not None and len(valor)>0:
        condiction = Q(nome__icontains = valor, status__gte = 1)
    else:
        condiction = Q(status__gte = 1)

    arr_list = Categoria.objects.filter(condiction)[:100000]

    for categoria in arr_list:
        Categoria.percentual = percentual(categoria.id)
        Categoria.total_gasto = total_gastos(categoria.id)
        Categoria.resta = resta(categoria.id)

    return render(request,"categorias_lista.html",{'arr_list':arr_list})

def categorias_del(request):
     id = request.GET.get('id')
     obj_categoria = Categoria.objects.get(id=id) #cria o objeto somente com o id correto
     obj_categoria.status = 0
     obj_categoria.save()
     return render(request,"categorias_apagou.html",{'id':id})

def categorias_edit(request):
    id = request.GET.get('id')
    obj_categoria = Categoria.objects.get(id=id)
    obj_categoria.meta = str(obj_categoria.meta)
    return render(request,"categorias_form.html",{'obj_categoria':obj_categoria})

