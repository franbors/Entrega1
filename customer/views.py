from http.client import HTTPResponse
from django.shortcuts import render
from customer.models import Cliente
from customer.forms import costumer_form
from django.http import HttpResponse

def clientes_view(request):
    return render(request, 'clientes_view.html')

def clientes_listado(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, "clientes_listado.html", context = context)


def clientes_crear(request):
    if request.method == 'GET':
        form = costumer_form()
        context = {'form' :form}
        return render(request, 'clientes_crear.html', context = context)
    else:
        form = costumer_form(request.POST)
        if form.is_valid():
            new_customer = Cliente.objects.create(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                pasaporte = form.cleaned_data['pasaporte'],
                vencimiento = form.cleaned_data['vencimiento'], 
                dni = form.cleaned_data['dni'],
                domicilio = form.cleaned_data['domicilio'], 
                telefono = form.cleaned_data['telefono']
            )
            context = {'new_customer' : new_customer}
        return render(request, 'clientes_crear.html', context = context)

def clientes_busqueda(request):
    cliente = Cliente.objects.filter(nombre__icontains = request.GET['search'])
    context = {'cliente':cliente}
    return render(request,'clientes_busqueda.html', context=context)