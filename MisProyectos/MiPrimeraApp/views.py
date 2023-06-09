from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

# Create your views here.

def inicio(request):
    n=1
    b=5
    resultado= n + b
    return HttpResponse(f"<h1>Bienvenido a mi primera web</h1><br><h2> El resultado de la suma es {resultado} </h2>")

def presentacion(request):
    return render(request, 'paginas/presentacion.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'paginas/index.html',{'libros' : libros})

def crear(request):
    formulario=LibroForm(request.POST or None, request.FILES or None)    
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')        
    return render(request, 'paginas/crear.html', {'formulario':formulario})
    
def editar(request, idParametro):
    libro= Libro.objects.get(id=idParametro)
    formulario=LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid and request.method=='POST':
        formulario.save()
        return redirect('libros')
    return render(request, 'paginas/editar.html', {'formulario':formulario})


def eliminar(request, idParametro):
    libro = Libro.objects.get(id=idParametro)
    libro.delete()
    return redirect('libros')