from django.urls import path
from MiNBA import views
from MiNBA.views import equipos, jugadores, historia

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("Franchises/", equipos.as_view(template_name = "MiNBA/equipos.html"), name="Franchises"),
    path("Players/", jugadores.as_view(template_name = "MiNBA/jugadores.html"), name="Players"),
    path("History/", historia.as_view(template_name = "MiNBA/historia.html"), name="History"),
    path("InsertFranchise/", views.equipoFormulario, name="InsertFranchise"),
    path("InsertPlayer/", views.jugadorFormulario, name="InsertPlayer"),
    path("InsertHistory/", views.historiaFormulario, name="InsertHistory"),
    path("SearchFranchise/", views.busquedaEquipo, name="SearchFranchise"),
    path("SearchF/", views.buscarEquipo),
    path("SearchPlayer/", views.busquedaJugador, name="SearchPlayer"),
    path("SearchP/", views.buscarJugador),
    path("SearchHistory/", views.busquedaHistoria, name="SearchHistory"),
    path("SearchH/", views.buscarHistoria),
]