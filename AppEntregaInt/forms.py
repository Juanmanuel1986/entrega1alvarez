from django import forms

class EquipoFormulario(forms.Form): # JM - creo una clase esto es lo que recibe la vista
    nombre = forms.CharField(max_length=100)
<<<<<<< HEAD
    aplicacion = forms.CharField(max_length=100)

#creo la clase para el unittest
class UnittestFormulario(forms.Form):
    coverage = forms.IntegerField()
    cantidadUT = forms.IntegerField()
=======
    aplicacion = forms.CharField(max_length=100)
>>>>>>> 28ea0a27e19e03cb81d0ed754a10d12d5759c3d3
