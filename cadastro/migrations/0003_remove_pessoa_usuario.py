# Generated by Django 3.0 on 2021-04-06 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20210405_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='usuario',
        ),
    ]
