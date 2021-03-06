# Generated by Django 2.0.5 on 2019-10-29 00:26

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gp', '0008_auto_20191028_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=15, verbose_name='Descrição')),
                ('nivel', models.IntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')], verbose_name='Nível')),
            ],
            options={
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='Remuneracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=15, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Remuneração',
                'verbose_name_plural': 'Remunerações',
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=15, verbose_name='Descrição')),
                ('remuneracao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gp.Remuneracao', verbose_name='Remuneração')),
                ('setor_pai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pai', to='gp.Setor', verbose_name='Setor Pai')),
            ],
            options={
                'ordering': ['descricao'],
                'verbose_name_plural': 'Setores',
            },
        ),
        migrations.CreateModel(
            name='TAE',
            fields=[
                ('servidor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gp.Servidor')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gp.Cargo')),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
                'verbose_name_plural': 'Docentes',
            },
            bases=('gp.servidor',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='servidor',
            name='fim',
            field=models.DateField(blank=True, help_text='Último dia que o servidor esteve em efetivo exercício no Campus.', null=True, verbose_name='Término do Exercício'),
        ),
        migrations.AlterField(
            model_name='servidor',
            name='inicio',
            field=models.DateField(help_text='Data em que o servidor entrou em efetivo exercício no Campus.', verbose_name='Início do Exercício'),
        ),
        migrations.AddField(
            model_name='servidor',
            name='setor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gp.Setor', verbose_name='Setor de Exercício'),
        ),
    ]
