from django.shortcuts import render, redirect
from .models import Reserva
from .forms import ReservaForm

def lista_reservas(request):
    sala = request.GET.get('sala')
    data = request.GET.get('data')

    reservas = Reserva.objects.all().order_by('data', 'horario_inicio')

    if sala:
        reservas = reservas.filter(sala__icontains=sala)

    if data:
        reservas = reservas.filter(data=data)

    return render(request, 'reservas/lista_reservas.html', {
        'reservas': reservas
    })

def nova_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm()

    return render(request, 'reservas/nova_reserva.html', {
        'form': form
    })