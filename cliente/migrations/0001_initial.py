# Generated by Django 3.2.9 on 2021-11-08 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(max_length=200)),
                ('endereco_cliente', models.CharField(max_length=300)),
                ('bairro_cliente', models.CharField(max_length=200)),
                ('cidade_cliente', models.CharField(max_length=300)),
                ('telefone_cliente', models.CharField(max_length=200)),
            ],
        ),
    ]
