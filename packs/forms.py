from django import forms
from packs.models import Paquete

class Paquete_form(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = '__all__'