from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context
import datetime
from AppEntregaInt.models import equipo
#from django.http.request import QueryDict

from AppEntregaInt.models import unittest,regressiontest
from AppEntregaInt.forms import UnittestFormulario,RegressiontestFormulario


# Create your views here.
"""def equipo(request):

      Equipo =  equipo(nombre="pp", nombreapp="sdsd")
      Equipo.save()
      documentoDeTexto = f"--->Curso: {equipo.nombre}   Camada: {equipo.nombreapp}"


      return HttpResponse(documentoDeTexto)"""


def inicio(request):
    #return HttpResponse('vista inicio')
    return render(request, "AppEntregaInt/inicio.html")

#def equipo(request):
    #return HttpResponse('vista equipo')    
    #return render(request, "AppEntregaInt/equipo.html")

def unittest2(request):
    #return HttpResponse('vista unittest')  
    return render(request, "AppEntregaInt/unittest.html")    

def regressiontest2(request):
    #return HttpResponse('vista regressiontest')  
    return render(request, "AppEntregaInt/regressiontest.html") 

#def equipoFormulario(request):
     # return render(request, "AppEntregaInt/equipoFormulario.html")


#def equipoFormulario(request):
 #     if request.method == 'POST':
  #    
   #         equipo =  equipo(request.post['nombre'],(request.post['aplicacion']))
#
 #           equipo.save()
#
 #           return render(request, "AppEntregaInt/inicio.html")
#
 #     return render(request,"AppEntregaInt/equipoFormulario.html") 



from AppEntregaInt.forms import EquipoFormulario

def equipoFormulario(request):

      if request.method == "POST":

            miFormulario = EquipoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  vequipo = equipo(nombre=informacion["nombre"], nombreapp=informacion["aplicacion"])
                  vequipo.save()
                  return render(request, "AppEntregaInt/inicio.html")
      else:
            miFormulario = EquipoFormulario()

      return render(request, "AppEntregaInt/equipoFormulario.html", {"miFormulario": miFormulario})      


def busquedaAplicacion(request):
      return render(request, "AppEntregaInt/busquedaAplicacion.html")


def buscar(request):

     # respuesta = f"Estoy buscando la aplicacion de nombre: {request.GET['nombreapp']}"

      #No olvidar from django.http import HttpResponse
      #return HttpResponse(respuesta)   
      #    
       if request.GET['nombreapp']:
            nombreapp = request.GET['nombreapp']
            equipos = equipo.objects.filter(nombreapp__icontains=nombreapp)
            
            return render(request, "AppEntregaInt/resultadosBusqueda.html", {"equipos":equipos, "nombreapp":nombreapp})

       
       else:
            respuesta = "mo enviaste datos"

       return HttpResponse(respuesta)     







#===================== AGREGO EL UNITTEST (antes cree el HTML)

def unittestFormulario(request):

      if request.method == "POST":

            miFormulario = UnittestFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  vunit = unittest(coverage=informacion["coverage"], cantidadUT=informacion["cantidadUT"])
                  vunit.save()
                  return render(request, "AppEntregaInt/inicio.html")
      else:
            miFormulario = UnittestFormulario()

      return render(request, "AppEntregaInt/unittestFormulario.html", {"miFormulario": miFormulario})      


#===================== AGREGO EL REGRESSIONTEST (antes cree el HTML)

def regressiontestFormulario(request):

      if request.method == "POST":

            miFormulario = RegressiontestFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  vrt = regressiontest(cantidadRT=informacion["cantidadRT"])
                  vrt.save()
                  return render(request, "AppEntregaInt/inicio.html")
      else:
            miFormulario = RegressiontestFormulario()

      return render(request, "AppEntregaInt/regressiontestFormulario.html", {"miFormulario": miFormulario})   