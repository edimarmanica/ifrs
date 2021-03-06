# Generated by Django 2.0.5 on 2019-11-03 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ensino_cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duracaoperiodo',
            name='descricao',
            field=models.CharField(max_length=10, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='eixotecnologico',
            name='descricao',
            field=models.CharField(max_length=50, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='modalidade',
            name='descricao',
            field=models.CharField(max_length=20, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='periodicidadeoferta',
            name='descricao',
            field=models.CharField(max_length=10, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='situacaocurso',
            name='descricao',
            field=models.CharField(max_length=50, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='tipocurso',
            name='descricao',
            field=models.CharField(max_length=30, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='tipooferta',
            name='descricao',
            field=models.CharField(max_length=50, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='turnofuncionamento',
            name='descricao',
            field=models.CharField(max_length=30, verbose_name='Descrição'),
        ),
    ]
