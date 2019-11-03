# Generated by Django 2.0.5 on 2019-11-03 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ensino_cursos', '0006_auto_20191103_1553'),
        ('gp', '0013_meuperfildocente'),
    ]

    operations = [
        migrations.CreateModel(
            name='AplicacaoAtividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data da substituição')),
                ('justificativa', models.TextField()),
                ('situacao', models.IntegerField(choices=[(0, 'Solicitado'), (1, 'Aceito pelo Substituto'), (2, 'Rejeitado pelo Substituto'), (3, 'Aprovado pela coordenação de ensino'), (4, 'Rejeitado pela coordenação de ensino'), (5, 'Cancelado')], default=0, verbose_name='Situação')),
                ('justificativa_substituto', models.TextField(blank=True, null=True)),
                ('justificativa_coord_ensino', models.TextField(blank=True, null=True)),
                ('componente_curricular', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ensino_cursos.ComponenteCurricular', verbose_name='Professor(a) solicitante')),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=15, verbose_name='Período - Turno')),
                ('horario_inicial', models.TimeField(verbose_name='Horário Inicial')),
                ('horario_final', models.TimeField(verbose_name='Horário Inicial')),
            ],
            options={
                'ordering': ['horario_inicial'],
                'verbose_name_plural': 'Períodos',
                'verbose_name': 'Período',
            },
        ),
        migrations.AddField(
            model_name='aplicacaoatividade',
            name='periodos',
            field=models.ManyToManyField(to='ensino_substituicoes.Periodo', verbose_name='Períodos'),
        ),
        migrations.AddField(
            model_name='aplicacaoatividade',
            name='solicitante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='solicitante', to='gp.Docente', verbose_name='Professor(a) solicitante'),
        ),
        migrations.AddField(
            model_name='aplicacaoatividade',
            name='substituto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='substituto', to='gp.Docente', verbose_name='Professor(a) substituto'),
        ),
    ]