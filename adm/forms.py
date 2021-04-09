from django import forms
from adm.models import Votar

class VotarForm(forms.ModelForm):
    class Meta:
        model = Votar
        fields = [
            "opcao"
        ]
