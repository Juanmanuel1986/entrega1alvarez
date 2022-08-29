from django.urls import path
from AppEntregaInt import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('equipo', views.equipo, name="equipo"),
<<<<<<< HEAD
    path('unittest', views.unittest2, name="unittest"),
    path('regressiontest', views.regressiontest2, name="regressiontest"),
=======
    path('unittest', views.unittest, name="unittest"),
    path('regressiontest', views.regressiontest, name="regressiontest"),
<<<<<<< HEAD
>>>>>>> 366ef49b5f7caea348c29b0c67d71a0f2d9cbcb3
    path('equipoFormulario', views.equipoFormulario, name="EquipoFormulario"), # primera clase form
    path('busquedaAplicacion',  views.busquedaAplicacion, name="BusquedaAplicacion"),#agrego busqueda
    path('buscar/', views.buscar), #busqueda
    path('unittestFormulario', views.unittestFormulario, name="unittestFormulario"),#segunda clase form
<<<<<<< HEAD
    path('regressiontestFormulario', views.regressiontestFormulario, name="regressiontestFormulario"),#segunda clase form

=======

=======
    path('equipoFormulario', views.equipoFormulario, name="EquipoFormulario"),
>>>>>>> 28ea0a27e19e03cb81d0ed754a10d12d5759c3d3
>>>>>>> 366ef49b5f7caea348c29b0c67d71a0f2d9cbcb3
]