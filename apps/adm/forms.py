from django import forms
from adm.models import FormularioDeContato

class ContatoFormulario(forms.ModelForm):
    class Meta:
        model = FormularioDeContato
        fields = '__all__'
