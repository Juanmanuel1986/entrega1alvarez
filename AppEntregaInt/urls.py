from django.urls import path
from AppEntregaInt import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('equipo', views.equipo, name="equipo"),
    path('unittest', views.unittest, name="unittest"),
    path('regressiontest', views.regressiontest, name="regressiontest"),
    path('equipoFormulario', views.equipoFormulario, name="EquipoFormulario"),
]