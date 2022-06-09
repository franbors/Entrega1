from django.shortcuts import render
from user.models import Usuario
from user.forms import Usuario_form
from user.models import Usuario

def usuarios_view(request):
    return render(request, 'usuarios_view.html')

def usuarios_listado(request):
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
    return render(request, "usuarios_listado.html", context = context)


def usuarios_crear(request):
    if request.method == 'GET':
        form = Usuario_form()
        context = {'form' :form}
        return render(request, 'usuarios_crear.html', context = context)
    else:
        form = Usuario_form(request.POST)
        if form.is_valid():
            nuevo_usuario = Usuario.objects.create(
                usertype = form.cleaned_data['usertype'],
                usuario = form.cleaned_data['usuario'],
                password = form.cleaned_data['password'],
                last_login = form.cleaned_data['last_login'], 
                activo = form.cleaned_data['activo']
            )
            context = {'nuevo_usuario' : nuevo_usuario}
        return render(request, 'usuarios_crear.html', context = context)

def usuarios_busqueda(request):
    usuario = Usuario.objects.filter(usuario__icontains = request.GET['search'])
    context = {'usuario':usuario}
    return render(request,'usuarios_busqueda.html', context=context)