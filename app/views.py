from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'index.html')

def turnos(request):
    t = turno.objects.all()
    lista={'turnos':t}
    return render(request, 'turnos.html',lista)

def eliminar_turno(request, id):
    t = turno.objects.get(id=id)
    t.delete()
    return redirect('turnos')

def doctores(request):
    return render(request, 'doctores.html')

def consultorios(request):
    return render(request, 'consultorios.html')
