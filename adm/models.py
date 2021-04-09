from django.db import models

class Votar(models.Model):

    pessoa = models.ForeignKey(
        "cadastro.Pessoa",
        verbose_name="Pessoa",
        on_delete=models.CASCADE,
    )

    votacao = models.ForeignKey(
        "cadastro.Votacao",
        verbose_name="Votação",
        on_delete=models.CASCADE,
    )

    opcao = models.ForeignKey(
        "cadastro.opcaoVoto",
        verbose_name="Opção",
        on_delete=models.CASCADE,
    )

    qtdVotos = models.IntegerField(
        "Quantidade de votos",
        null=True,
        blank=True,
        default=0,
    )

    class Meta:
        verbose_name = "Votar"
        verbose_name_plural = "Votar"

    def __str__(self):
        return self.pessoa.nome_completo 
