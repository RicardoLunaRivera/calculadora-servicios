from django.urls import path
from .views import index, mostrar_servicios, mostrar_servicio, calcular_costo_total

urlpatterns = [
    path('', index, name='inicio'),
    path('servicios/', mostrar_servicios, name='servicios'),
    path('servicio/<int:id>', mostrar_servicio, name='servicio' ),
    path('calcular-costo-total/', calcular_costo_total, name='calcular_costo_total'),
]