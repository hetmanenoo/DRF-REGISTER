# Generated by Django 4.1.2 on 2022-11-28 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.AddField(
            model_name='register',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='register',
            name='login',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
