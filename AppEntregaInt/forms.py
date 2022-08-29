from django import forms

class EquipoFormulario(forms.Form): # JM - creo una clase esto es lo que recibe la vista
    nombre = forms.CharField(max_length=100)
    aplicacion = forms.CharField(max_length=100)

#creo la clase para el unittest
class UnittestFormulario(forms.Form):
    coverage = forms.IntegerField()
    cantidadUT = forms.IntegerField()

#creola clase para regressiontest
class RegressiontestFormulario(forms.Form):
    cantidadRT = forms.IntegerField()
 