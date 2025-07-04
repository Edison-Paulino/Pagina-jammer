# Generated by Django 5.2.2 on 2025-07-01 23:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_frecuenciacontrol_logacciones'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroJammer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frecuencia_mhz', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ubicacion', models.CharField(blank=True, max_length=100)),
                ('inicio_registro', models.DateTimeField()),
                ('fin_registro', models.DateTimeField(blank=True, null=True)),
                ('usuario_fin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='registros_finalizados', to=settings.AUTH_USER_MODEL)),
                ('usuario_inicio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='registros_iniciados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
