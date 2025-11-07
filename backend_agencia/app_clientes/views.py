from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .models import Transporte
from django.urls import reverse
from django.utils import timezone

def inicio_agencia(request):
    # página principal de la app
    return render(request, 'inicio.html', {})

def agregar_clientes(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        apellido = request.POST.get('apellido', '').strip()
        correo = request.POST.get('correo', '').strip() or None
        telefono = request.POST.get('telefono', '').strip() or None
        direccion = request.POST.get('direccion', '').strip() or None
        fecha_nacimiento = request.POST.get('fecha_nacimiento') or None

        cliente = Cliente(
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            telefono=telefono,
            direccion=direccion,
            fecha_nacimiento=fecha_nacimiento
        )
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'clientes/agregar_clientes.html', {})

def ver_clientes(request):
    clientes = Cliente.objects.all().order_by('apellido', 'nombre')
    return render(request, 'clientes/ver_clientes.html', {'clientes': clientes})

def actualizar_clientes(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/actualizar_clientes.html', {'cliente': cliente})

def realizar_actualizacion_clientes(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre', cliente.nombre).strip()
        cliente.apellido = request.POST.get('apellido', cliente.apellido).strip()
        correo = request.POST.get('correo', '').strip()
        cliente.correo = correo or None
        telefono = request.POST.get('telefono', '').strip()
        cliente.telefono = telefono or None
        direccion = request.POST.get('direccion', '').strip()
        cliente.direccion = direccion or None
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        cliente.fecha_nacimiento = fecha_nacimiento or None
        cliente.save()
        return redirect('ver_clientes')
    # si llama GET, redirigir a formulario de edición
    return redirect('actualizar_clientes', cliente_id=cliente.id)

def borrar_clientes(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'clientes/borrar_clientes.html', {'cliente': cliente})

def agregar_transportes(request):
    if request.method == 'POST':
        nombre_transporte = request.POST.get('nombre_transporte', '').strip()
        descripcion = request.POST.get('descripcion', '').strip() or None
        tipo = request.POST.get('tipo', '').strip() or None
        capacidad = request.POST.get('capacidad') or None
        precio = request.POST.get('precio') or None
        horario = request.POST.get('horario') or None
        empresa = request.POST.get('empresa', '').strip() or None

        # convertir capacidad y precio si vienen vacíos
        capacidad_val = int(capacidad) if capacidad else None
        precio_val = precio if precio else None  # DB lo convertirá según DecimalField

        transporte = Transporte(
            nombre_transporte=nombre_transporte,
            descripcion=descripcion,
            tipo=tipo,
            capacidad=capacidad_val,
            precio=precio_val,
            horario=horario or None,
            empresa=empresa
        )
        transporte.save()
        return redirect('ver_transportes')
    return render(request, 'transportes/agregar_transportes.html', {})

def ver_transportes(request):
    transportes = Transporte.objects.all().order_by('nombre_transporte')
    return render(request, 'transportes/ver_transportes.html', {'transportes': transportes})

def actualizar_transportes(request, transporte_id):
    transporte = get_object_or_404(Transporte, id=transporte_id)
    return render(request, 'transportes/actualizar_transportes.html', {'transporte': transporte})

def realizar_actualizacion_transportes(request, transporte_id):
    transporte = get_object_or_404(Transporte, id=transporte_id)
    if request.method == 'POST':
        transporte.nombre_transporte = request.POST.get('nombre_transporte', transporte.nombre_transporte).strip()
        descripcion = request.POST.get('descripcion', '').strip()
        transporte.descripcion = descripcion or None
        tipo = request.POST.get('tipo', '').strip()
        transporte.tipo = tipo or None
        capacidad = request.POST.get('capacidad')
        transporte.capacidad = int(capacidad) if capacidad else None
        precio = request.POST.get('precio')
        transporte.precio = precio if precio else None
        horario = request.POST.get('horario')
        transporte.horario = horario or None
        empresa = request.POST.get('empresa', '').strip()
        transporte.empresa = empresa or None
        transporte.save()
        return redirect('ver_transportes')
    return redirect('actualizar_transportes', transporte_id=transporte.id)

def borrar_transportes(request, transporte_id):
    transporte = get_object_or_404(Transporte, id=transporte_id)
    if request.method == 'POST':
        transporte.delete()
        return redirect('ver_transportes')
    return render(request, 'transportes/borrar_transportes.html', {'transporte': transporte})