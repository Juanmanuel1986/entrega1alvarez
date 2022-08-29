from django import forms

class EquipoFormulario(forms.Form): # JM - creo una clase esto es lo que recibe la vista
    nombre = forms.CharField(max_length=100)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 366ef49b5f7caea348c29b0c67d71a0f2d9cbcb3
    aplicacion = forms.CharField(max_length=100)

#creo la clase para el unittest
class UnittestFormulario(forms.Form):
    coverage = forms.IntegerField()
    cantidadUT = forms.IntegerField()
<<<<<<< HEAD

#creola clase para regressiontest
class RegressiontestFormulario(forms.Form):
    cantidadRT = forms.IntegerField()
 
=======
=======
    aplicacion = forms.CharField(max_length=100)
>>>>>>> 28ea0a27e19e03cb81d0ed754a10d12d5759c3d3
>>>>>>> 366ef49b5f7caea348c29b0c67d71a0f2d9cbcb3
