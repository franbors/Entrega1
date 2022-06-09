from django import forms
from user.models import Usuario

class Usuario_form(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'