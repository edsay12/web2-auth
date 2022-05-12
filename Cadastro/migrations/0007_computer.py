# Generated by Django 3.2.9 on 2021-12-09 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastro', '0006_artigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False, verbose_name='Código')),
                ('data', models.DateField()),
                ('horario', models.DateTimeField()),
                ('nome', models.CharField(max_length=50)),
                ('matricula', models.CharField(max_length=6, verbose_name='Matrícula')),
            ],
        ),
    ]
