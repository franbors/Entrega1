from django.contrib import admin
from django.urls import path, include
from customer.views import *
from final.views import *
from packs.views import *
from customer.views import *
from user.views import *

urlpatterns = [
    path('', index_view, name = 'index_view'),
    path('paquetes/', paquetes_view, name = 'paquetes_view'),
    path('paquetes-listado/', paquetes_listado, name = 'paquetes_listado'),
    path('paquete_crear/', paquetes_crear, name = 'paquetes_crear'),
    path('paquetes-busqueda/', paquetes_busqueda, name = 'paquetes_busqueda'),
    path('usuarios/', usuarios_view, name = 'usuarios_view'),
    path('usuarios-listado/', usuarios_listado, name = 'usuarios_listado'),
    path('usuarios-crear/', usuarios_crear, name = 'usuarios_crear'),
    path('usuarios-busqueda/', usuarios_busqueda, name = 'usuarios_busqueda'),
    path('clientes/', clientes_view, name = 'clientes_view'),
    path('clientes-listado/', clientes_listado, name = 'clientes_listado'),
    path('clientes-crear/', clientes_crear, name = 'clientes_crear'),
    path('clientes-busqueda/', clientes_busqueda, name = 'clientes_busqueda'),
    
    path('admin/', admin.site.urls)    
]
