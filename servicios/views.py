from django.http import JsonResponse
from django.shortcuts import render
from .models import Servicio


# Create your views here.
def index(request):
    return render(request, 'index.html')


def mostrar_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'mostrar_servicios.html', {'servicios': servicios})


def mostrar_servicio(request, id):
    servicio = Servicio.objects.get(id=id)
    return render(request, 'mostrar_servicio.html', {'servicio': servicio})


def calcular_costo_total(request):
    cantidad = int(request.GET.get('cantidad', 1))  # Obtener la cantidad de servicios
    servicio_id = int(request.GET.get('servicio_id', 1))  # Obtener el ID del servicio seleccionado
    try:
        servicio = Servicio.objects.get(id=servicio_id)  # Obtener el objeto del servicio desde la base de datos
        costo_servicio = servicio.costo  # Obtener el costo del servicio
        costo_total = cantidad * costo_servicio  # Calcular el costo total
        return JsonResponse({'costo_total': costo_total})
    except Servicio.DoesNotExist:
        return JsonResponse({'error': 'El servicio no existe'})