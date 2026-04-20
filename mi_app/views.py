from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'lista.html', {'tareas': tareas})

def crear_tarea(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        Tarea.objects.create(titulo=titulo, descripcion=descripcion)
        return redirect('lista')
    return render(request, 'crear.html')

def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        tarea.titulo = request.POST['titulo']
        tarea.descripcion = request.POST['descripcion']
        tarea.save()
        return redirect('lista')
    return render(request, 'editar.html', {'tarea': tarea})

def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.delete()
    return redirect('lista')# Create your views here.
