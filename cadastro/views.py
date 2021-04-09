from django.shortcuts import render, redirect
from cadastro.forms import *
from django.contrib import messages

def registrar_pessoa(request):

    form = PessoaForm()

    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid():
            form.save()

        messages.success(
            request,
            "Pessoa salva com sucesso",
        )

        return redirect("home")

    context = {
        "nome_pagina": "Cadastro Pessoa",
        "form": form,
    }

    return render(request, "registrar_pessoa.html", context)

def registrar_votacao(request):

    form = VotacaoForm()

    if request.method == "POST":
        form = VotacaoForm(request.POST)

        if form.is_valid():
            form.save()

        messages.success(
            request,
            "Votação salva com sucesso",
        )

        return redirect("home")    

    context = {
        "nome_pagina": "Cadastro Votação",
        "form": form,
    }

    return render(request, "registrar_votacao.html", context)

def registrar_opcaoVoto(request):

    form = OpcaoVotoForm()

    if request.method == "POST":
        form = OpcaoVotoForm(request.POST)

        if form.is_valid():
            form.save()

        messages.success(
            request,
            "Opçao de voto salva com sucesso",
        )

        return redirect("home")

    context = {
        "nome_pagina": "Cadastro Opção de Voto",
        "form": form,
    }

    return render(request, "registrar_opcaoVoto.html", context)