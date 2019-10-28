# Generated by Django 2.0.5 on 2019-10-28 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Titulacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Titulação',
                'verbose_name_plural': 'Titulações',
                'ordering': ['descricao'],
            },
        ),
    ]