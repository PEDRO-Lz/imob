# Generated by Django 4.2.7 on 2023-11-20 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appimob', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='proprietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imoveis_possuidos', to=settings.AUTH_USER_MODEL),
        ),
    ]
