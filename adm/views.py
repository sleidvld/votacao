from django.shortcuts import render, redirect
from adm.forms import *
from django.contrib import messages
from cadastro.models import *


def validacao(request, id_votacao):
    
    if request.POST:
        objCpf = request.POST.get('cpf',None)
        objVotacao = Votacao.objects.get(pk=id_votacao)
        try:
            objPessoa = Pessoa.objects.get(cpf = objCpf)
            objVotar = Votar.objects.filter(votacao=objVotacao,pessoa=objPessoa)
            if objVotacao.voto_unico and objVotar:
                messages.error(request,
                "Essa votação é voto unico",
                )
                return redirect("validacao", id_votacao)
                
            messages.error(request,
            "CPF valido",
            )
            return redirect("votar", id_votacao, objPessoa.id)

        except Pessoa.DoesNotExist:
            messages.error(request,
            "CPF não econtrado",
            )

            return redirect("validacao",id_votacao)
        
    context = {
        "nome_pagina": "Validação",
    }

    return render(request, "votar_validacao.html", context)


def votar(request,id_votacao,id_pessoa):

    todas_opcoes = OpcaoVoto.objects.filter(votacao__id=id_votacao)

    if request.POST:
        objVotacao = Votacao.objects.get(pk=id_votacao)
        objPessoa = Pessoa.objects.get(pk=id_pessoa)
        voto = request.POST.get('opcao_voto',None)
        objOpcao = OpcaoVoto.objects.get(pk=voto)
        objOpcao.numero_votos += 1
        objOpcao.save()
        try:
            objVotar = Votar.objects.get(pessoa=objPessoa,votacao=objVotacao,opcao=objOpcao)

            return redirect("home")
        except Votar.DoesNotExist:
            objVotar = Votar()
            objVotar.pessoa = objPessoa
            objVotar.votacao = objVotacao
            objVotar.opcao = objOpcao

        objVotar.qtdVotos += 1
        objVotar.save()

        messages.success(
            request,
            "Voto bem-sucedido",
        )

        return redirect("home")

    context = {
        "nome_pagina": "Votação",
        "todas_opcoes": todas_opcoes,
    }

    return render(request, "votar.html", context)


def apuracao(request, id_votacao):

    todas_opcoes = OpcaoVoto.objects.filter(votacao__id=id_votacao)

    context = {
        "nome_pagina": "Apuração",
        "todas_opcoes": todas_opcoes,
    }

    return render(request, "apuracao.html", context)


def quem_votou(request, id_opcao):

    Votos = Votar.objects.filter(opcao=id_opcao)

    context = {
        "nome_pagina": "Quem Votou",
        "votos": Votos,
    }

    return render(request, "quem_votou.html", context)




