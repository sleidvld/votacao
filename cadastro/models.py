from django.db import models

class Pessoa(models.Model):

    nome_completo = models.CharField(
        verbose_name="Nome completo",
        max_length=194,
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,
        auto_now_add=False,
    )

    email = models.EmailField(
        verbose_name="Email do usuario",
        max_length=194,
        unique=True,
    )

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.nome_completo 

class Votacao(models.Model):

    nome = models.CharField(
        verbose_name="Nome Votação",
        max_length=194,
    )

    descricao = models.CharField(
        verbose_name="Descrição da votação",
        max_length=200,
    )

    anonimo = models.BooleanField(
        verbose_name="Pode ser anonimo",
        default=False,
    )

    voto_unico = models.BooleanField(
        verbose_name="Voto Unico",
        default=False,
    )

    data_inicio = models.DateField(
        verbose_name="Data de inicio",
        auto_now=False,
        auto_now_add=False,
    )

    data_termino = models.DateField(
        verbose_name="Data de termino",
        auto_now=False,
        auto_now_add=False,
    )

    class Meta:
        verbose_name = "Votação"
        verbose_name_plural = "Votações"

    def __str__(self):
        return self.nome

class OpcaoVoto(models.Model):

    nome = models.CharField(
        verbose_name="Nome Opção de voto",
        max_length=194,
        null=False,
    )

    votacao = models.ForeignKey(
        Votacao,
        verbose_name= "Votação",
        on_delete=models.CASCADE,
    )

    codigo = models.CharField(
        verbose_name="Codigo",
        max_length=3,
    )

    numero_votos = models.IntegerField(
        "Numero de votos",
        null=True,
        blank=True,
        default=0,
    )

    class Meta:
        verbose_name = "Opção de voto"
        verbose_name_plural = "Opçṍes de voto"

    def __str__(self):
        return self.nome