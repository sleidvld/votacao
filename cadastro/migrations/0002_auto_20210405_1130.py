# Generated by Django 3.0 on 2021-04-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opcaovoto',
            name='qtd_votos',
        ),
        migrations.AddField(
            model_name='opcaovoto',
            name='numero_votos',
            field=models.IntegerField(blank=True, null=True, verbose_name='Numero de votos'),
        ),
        migrations.AlterField(
            model_name='votacao',
            name='descricao',
            field=models.CharField(max_length=200, verbose_name='Descrição da votação'),
        ),
    ]
