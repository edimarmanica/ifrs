# Generated by Django 2.0.5 on 2019-10-26 23:48

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servidores', '0002_auto_20191026_2344'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='servidor',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='servidor',
            name='id',
        ),
        migrations.RemoveField(
            model_name='servidor',
            name='user',
        ),
        migrations.AddField(
            model_name='servidor',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=1234, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]