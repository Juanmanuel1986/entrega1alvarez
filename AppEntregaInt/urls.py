from django.urls import path
from AppEntregaInt import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('equipo', views.equipo, name="equipo"),
    path('unittest', views.unittest2, name="unittest"),
    path('regressiontest', views.regressiontest2, name="regressiontest"),
    path('equipoFormulario', views.equipoFormulario, name="EquipoFormulario"), # primera clase form
    path('busquedaAplicacion',  views.busquedaAplicacion, name="BusquedaAplicacion"),#agrego busqueda
    path('buscar/', views.buscar), #busqueda
    path('unittestFormulario', views.unittestFormulario, name="unittestFormulario"),#segunda clase form
    path('regressiontestFormulario', views.regressiontestFormulario, name="regressiontestFormulario"),#segunda clase form

]