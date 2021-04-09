from django.shortcuts import render
from cadastro.models import Votacao
import datetime

def home(request):
    
    hoje = datetime.date.today()
    todas_votacoes = Votacao.objects.all()

    context = {
        "todas_votacoes": todas_votacoes,
        "nome_pagina": "Inicio",
        "hoje":hoje,
    }

    return render(request, "home.html", context,)
