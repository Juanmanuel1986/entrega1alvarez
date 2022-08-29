from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context
import datetime
from AppEntregaInt.models import equipo
<<<<<<< HEAD
#from django.http.request import QueryDict

from AppEntregaInt.models import unittest
from AppEntregaInt.forms import UnittestFormulario

=======
<<<<<<< HEAD
#from django.http.request import QueryDict
=======
>>>>>>> ac3d0567313ae445a66f34f1c0359812bedb9e20
>>>>>>> 28ea0a27e19e03cb81d0ed754a10d12d5759c3d3

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

#def unittest(request):
    #return HttpResponse('vista unittest')  
   # return render(request, "AppEntregaInt/unittest.html")    

def regressiontest(request):
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
<<<<<<< HEAD
                  vequipo = equipo(nombre=informacion["nombre"], nombreapp=informacion["aplicacion"])
                  vequipo.save()
=======
<<<<<<< HEAD
                  vequipo = equipo(nombre=informacion["nombre"], nombreapp=informacion["aplicacion"])
                  vequipo.save()
=======
                  variable = equipo(nombre=informacion["nombre"], nombreapp=informacion["aplicacion"])
                  variable.save()
>>>>>>> ac3d0567313ae445a66f34f1c0359812bedb9e20
>>>>>>> 28ea0a27e19e03cb81d0ed754a10d12d5759c3d3
                  return render(request, "AppEntregaInt/inicio.html")
      else:
            miFormulario = EquipoFormulario()

<<<<<<< HEAD
      return render(request, "AppEntregaInt/equipoFormulario.html", {"miFormulario": miFormulario})      


def busquedaAplicacion(request):
      return render(request, "AppEntregaInt/busquedaAplicacion.html")


def buscar(request):

      respuesta = f"Estoy buscando la aplicacion de nombre: {request.GET['nombreapp']}"

      #No olvidar from django.http import HttpResponse
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
=======
      return render(request, "AppEntregaInt/equipoFormulario.html", {"miFormulario": miFormulario})      
>>>>>>> 28ea0a27e19e03cb81d0ed754a10d12d5759c3d3
