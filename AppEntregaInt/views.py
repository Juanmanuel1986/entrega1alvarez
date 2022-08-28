from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context
import datetime
from AppEntregaInt.models import equipo

# Create your views here.

def inicio(request):
    #return HttpResponse('vista inicio')
    return render(request, "AppEntregaInt/inicio.html")

def equipo(request):
    #return HttpResponse('vista equipo')    
    return render(request, "AppEntregaInt/equipo.html")

def unittest(request):
    #return HttpResponse('vista unittest')  
    return render(request, "AppEntregaInt/unittest.html")    

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
                  variable = equipo(nombre=informacion["nombre"], nombreapp=informacion["aplicacion"])
                  variable.save()
                  return render(request, "AppEntregaInt/inicio.html")
      else:
            miFormulario = EquipoFormulario()

      return render(request, "AppEntregaInt/equipoFormulario.html", {"miFormulario": miFormulario})      