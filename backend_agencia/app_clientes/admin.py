from django.contrib import admin
from .models import Cliente, Transporte  # importa Transporte

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','correo','telefono')
    search_fields = ('nombre','apellido','correo')

@admin.register(Transporte)
class TransporteAdmin(admin.ModelAdmin):
    list_display = ('nombre_transporte', 'tipo', 'capacidad', 'empresa', 'precio')
    search_fields = ('nombre_transporte','empresa','tipo')
