from django import forms

class costumer_form(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    pasaporte = forms.IntegerField()
    vencimiento = forms.DateField()
    dni = forms.IntegerField()
    domicilio = forms.CharField(max_length=40)
    telefono = forms.IntegerField()