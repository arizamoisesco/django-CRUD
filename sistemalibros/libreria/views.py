from socket import fromfd
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibrosForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crear_libro(request):
    formulario = LibrosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar_libro(request):
    return render(request, 'libros/editar.html')
