from django.urls import path
from AppEntregaInt import views

urlpatterns = [
    path('', views.inicio),
    path('equipo', views.equipo),
    path('unittest', views.unittest),
    path('regressiontest', views.regressiontest),
]