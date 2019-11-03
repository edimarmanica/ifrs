# Generated by Django 2.0.5 on 2019-11-03 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DuracaoPeriodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=15, verbose_name='Descrição')),
            ],
            options={
                'ordering': ['descricao'],
                'verbose_name_plural': 'Durações dos Períodos',
                'verbose_name': 'Duração do Período',
            },
        ),
        migrations.CreateModel(
            name='EixoTecnologico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=15, verbose_name='Descrição')),
            ],
            options={
                'ordering': ['descricao'],
                'verbose_name_plural': 'Eixos Tecnológicos',
                'verbose_name': 'Eixo Tecnológico',
            },
        ),
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=15, verbose_name='Descrição')),
            ],
            options={
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='PeriodicidadeOferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=15, verbose_name='Descrição')),
            ],
            options={
                'ordering': ['descricao'],
                'verbose_name_plural': 'Periodicidades de Oferta',
                'verbose_name': 'Periodicidade de Oferta',
            },
        ),
        migrations.CreateModel(
            name='SituacaoCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=15, verbose_name='Descrição')),
            ],
            options={
                'ordering': ['descricao'],
                'verbose_name_plural': 'Situações dos Cursos',
                'verbose_name': 'Situação do Curso',
            },
        ),
        migrations.CreateModel(
            name='TipoCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=15, verbose_name='Descrição')),
            ],
            options={
                'ordering': ['descricao'],
                'verbose_name_plural': 'Tipos de Cursos',
                'verbose_name': 'Tipo de Curso',
            },
        ),
        migrations.CreateModel(
            name='TipoOferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=15, verbose_name='Descrição')),
            ],
            options={
                'ordering': ['descricao'],
                'verbose_name_plural': 'Tipos de Ofertas',
                'verbose_name': 'Tipo de Oferta',
            },
        ),
        migrations.CreateModel(
            name='TurnoFuncionamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=15, verbose_name='Descrição')),
            ],
            options={
                'ordering': ['descricao'],
                'verbose_name_plural': 'Turnos de Funcionamento',
                'verbose_name': 'Turno de Funcionamento',
            },
        ),
    ]
