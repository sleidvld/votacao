from django import forms
from cadastro.models import *

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = [
            "nome_completo", "data_nascimento", "cpf",
            "email"
        ]

class VotacaoForm(forms.ModelForm):
    class Meta:
        model = Votacao
        fields = "__all__"

class OpcaoVotoForm(forms.ModelForm):
    class Meta:
        model = OpcaoVoto
        fields = [
            "nome", "votacao", "codigo" 
        ]