from unicodedata import name
from django.shortcuts import render
from MiNBA.forms import equiposFormulario, jugadoresFormulario, temporadaFormulario
from MiNBA.models import Franquicia, Jugador, Temporada
from django.views.generic import ListView
# Create your views here.

def inicio(request):
    
    return render(request, "MiNBA/inicio.html")

class equipos(ListView):

    model = Franquicia

class jugadores(ListView):

    model = Jugador

class historia(ListView):

    model = Temporada

def equipoFormulario(request):
    
    if request.method == "POST":
        
        miFormulario = equiposFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            equipo = Franquicia(nombre=informacion["nombre"], ciudad=informacion["ciudad"], estadio=informacion["estadio"], campeonatos=informacion["campeonatos"], ultcampeonato=informacion["ultcampeonato"], colores=informacion["colores"])

            equipo.save()

            return render(request, "MiNBA/equipos.html")
    
    else:

        miFormulario = equiposFormulario()
    
    return render(request, "MiNBA/equiposFormulario.html", {"miFormulario":miFormulario})

def jugadorFormulario(request):
    
    if request.method == "POST":
        
        miFormulario = jugadoresFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            jugador = Jugador(nombre=informacion["nombre"], apellido=informacion["apellido"], edad=informacion["edad"], nacionalidad=informacion["nacionalidad"], equipoact=informacion["equipoact"], equipos=informacion["equipos"], campeonatos=informacion["campeonatos"], allstar=informacion["allstar"])

            jugador.save()

            return render(request, "MiNBA/jugadores.html")
    
    else:
        
        miFormulario = jugadoresFormulario()
    
    return render(request, "MiNBA/jugadoresFormulario.html", {"miFormulario":miFormulario})

def historiaFormulario(request):
    
    if request.method == "POST":
        
        miFormulario = temporadaFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            temporada = Temporada(temporada=informacion["temporada"], campeon=informacion["campeon"], sub=informacion["sub"], serie=informacion["serie"], fmvp=informacion["fmvp"], mvp=informacion["mvp"], record=informacion["record"], defensa=informacion["defensa"])

            temporada.save()

            return render(request, "MiNBA/historia.html")
    
    else:
        
        miFormulario = temporadaFormulario()
    
    return render(request, "MiNBA/historiaFormulario.html", {"miFormulario":miFormulario})

def busquedaEquipo(request):

    return render(request, "MiNBA/busquedaEquipo.html")

def buscarEquipo(request):

    if request.GET["ciudad"]:

        ciudad = request.GET["ciudad"]
        franquicias = Franquicia.objects.filter(ciudad__icontains=ciudad)

        return render(request, "MiNBA/resultadosBusquedaEquipo.html", {"franquicias":franquicias, "ciudad":ciudad})
    
    else:

        respuesta = "No enviaste datos"

    return render(request, "MiNBA/resultadosBusquedaEquipo.html", {"respuesta":respuesta})

def busquedaJugador(request):

    return render(request, "MiNBA/busquedaJugador.html")

def buscarJugador(request):

    if request.GET["apellido"]:

        apellido = request.GET["apellido"]
        jugadores = Jugador.objects.filter(apellido__icontains=apellido)

        return render(request, "MiNBA/resultadosBusquedaJugador.html", {"jugadores":jugadores, "apellido":apellido})
    
    else:

        respuesta = "No enviaste datos"

    return render(request, "MiNBA/resultadosBusquedaJugador.html", {"respuesta":respuesta})

def busquedaHistoria(request):

    return render(request, "MiNBA/busquedaHistoria.html")

def buscarHistoria(request):

    if request.GET["temporada"]:

        temporada = request.GET["temporada"]
        campeones = Temporada.objects.filter(temporada__icontains=temporada)

        return render(request, "MiNBA/resultadosBusquedaHistoria.html", {"campeones":campeones, "temporada":temporada})
    
    else:

        respuesta = "No enviaste datos"

    return render(request, "MiNBA/resultadosBusquedaHistoria.html", {"respuesta":respuesta})