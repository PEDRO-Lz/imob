from django import forms
from .models import Proprietario, Locatario, Imovel, User

class ProprietarioForm(forms.ModelForm):
    class Meta:
        model = Proprietario
        fields = []

class LocatarioForm(forms.ModelForm):
    class Meta:
        model = Locatario
        fields = ['cpf']


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = ['tipo', 'preco']

class EditarNomeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name']