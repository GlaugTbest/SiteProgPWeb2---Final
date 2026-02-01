from django.urls import path
from .views import lista_reservas, nova_reserva

urlpatterns = [
    path('', lista_reservas, name='lista_reservas'),
    path('nova/', nova_reserva, name='nova_reserva'),
]