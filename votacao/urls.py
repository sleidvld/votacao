
from django.contrib import admin
from django.urls import path

from usuarios.views import home
from cadastro.views import *
from adm.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        '',
        home,
        name="home",
    ),

    path(
        'registrar-pessoa/',
        registrar_pessoa,
        name="registrar_pessoa",
    ),

    path(
        'registrar-votacao/',
        registrar_votacao,
        name="registrar_votacao",
    ),

    path(
        'registrar-opcaoVoto/',
        registrar_opcaoVoto,
        name="registrar_opcaoVoto",
    ),

    path(
        'votacao/<int:id_votacao>/<int:id_pessoa>',
        votar,
        name="votar",
    ),

    path(
        'validacao/<int:id_votacao>',
        validacao,
        name="validacao",
    ),

    path(
        'apuracao/<int:id_votacao>',
        apuracao,
        name="apuracao",
    ),

    path(
        'quem_votou/<int:id_opcao>',
        quem_votou,
        name="quem_votou",
    ),

]
