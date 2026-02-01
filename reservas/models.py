from django.db import models

class Reserva(models.Model):
    sala = models.CharField(max_length=50)
    data = models.DateField()
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.sala} - {self.data}"