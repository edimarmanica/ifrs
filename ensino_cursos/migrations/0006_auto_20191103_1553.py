# Generated by Django 2.0.5 on 2019-11-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ensino_cursos', '0005_auto_20191103_1546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='componentecurricular',
            options={'ordering': ['denominacao'], 'verbose_name': 'Componente Curricular', 'verbose_name_plural': 'Componentes Curriculares'},
        ),
        migrations.AlterField(
            model_name='componentecurricular',
            name='denominacao',
            field=models.CharField(max_length=30, verbose_name='Denominação'),
        ),
    ]
