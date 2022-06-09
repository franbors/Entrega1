from django.shortcuts import render
from packs.forms import Paquete_form
from packs.models import Paquete

def paquetes_view(request):
    return render(request, 'paquetes_view.html')

def paquetes_listado(request):
    paquetes = Paquete.objects.all()
    context = {'paquetes': paquetes}
    return render(request, "paquetes_listado.html", context = context)


def paquetes_crear(request):
    if request.method == 'GET':
        form = Paquete_form()
        context = {'form' :form}
        return render(request, 'paquetes_crear.html', context = context)
    else:
        form = Paquete_form(request.POST)
        if form.is_valid():
            nuevo_paquete = Paquete.objects.create(
                destino = form.cleaned_data['destino'],
                descripcion = form.cleaned_data['descripcion'],
                dias = form.cleaned_data['dias'],
                fecha_partida = form.cleaned_data['fecha_partida'], 
                fecha_regreso = form.cleaned_data['fecha_regreso'],
                Image_Set_1 = form.cleaned_data['Image_Set_1'], 
                Image_Set_2 = form.cleaned_data['Image_Set_2'],
                precio_publico = form.cleaned_data['precio_publico'],
                costo = form.cleaned_data['costo'],
                oferta = form.cleaned_data['oferta'],
                activo = form.cleaned_data['activo'],
            )
            context = {'nuevo_paquete' : nuevo_paquete}
        return render(request, 'paquetes_crear.html', context = context)

def paquetes_busqueda(request):
    paquete = Paquete.objects.filter(destino__icontains = request.GET['search'])
    context = {'paquete':paquete}
    return render(request,'paquetes_busqueda.html', context=context)