from django import forms

class equiposFormulario(forms.Form):

    nombre = forms.CharField()
    ciudad = forms.CharField()
    estadio = forms.CharField()
    campeonatos = forms.IntegerField()
    ultcampeonato = forms.IntegerField()
    colores = forms.CharField()

class jugadoresFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.CharField()
    nacionalidad = forms.CharField()
    equipoact = forms.CharField()
    equipos = forms.CharField()
    campeonatos = forms.CharField()
    allstar = forms.CharField()

class temporadaFormulario(forms.Form):

    temporada = forms.CharField()
    campeon = forms.CharField()
    sub = forms.CharField()
    serie = forms.CharField()
    fmvp = forms.CharField()
    mvp = forms.CharField()
    record = forms.CharField()
    defensa = forms.CharField()