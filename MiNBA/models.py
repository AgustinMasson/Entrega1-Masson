from django.db import models

# Create your models here.

class Franquicia(models.Model):

    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    estadio = models.CharField(max_length=100)
    campeonatos = models.IntegerField()
    ultcampeonato = models.IntegerField()
    colores = models.CharField(max_length=100)

class Jugador(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    equipoact = models.CharField(max_length=100)
    equipos = models.CharField(max_length=100)
    campeonatos = models.CharField(max_length=100)
    allstar = models.CharField(max_length=100)

class Temporada(models.Model):

    temporada = models.CharField(max_length=100)
    campeon = models.CharField(max_length=100)
    sub = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)
    fmvp = models.CharField(max_length=100)
    mvp = models.CharField(max_length=100)
    record = models.CharField(max_length=100)
    defensa = models.CharField(max_length=100)