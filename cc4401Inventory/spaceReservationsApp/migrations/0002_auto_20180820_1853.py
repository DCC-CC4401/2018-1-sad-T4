# Generated by Django 2.0.5 on 2018-08-20 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spaceReservationsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spacereservation',
            name='admin',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spacereservation_admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='spacereservation',
            name='finish_state',
            field=models.CharField(choices=[('L', 'Perdido'), ('E', 'Recibido'), ('I', 'Indefinido')], default='I', max_length=1, verbose_name='Estado de finalización'),
        ),
        migrations.AlterField(
            model_name='spacereservation',
            name='state',
            field=models.CharField(choices=[('A', 'Aceptado'), ('R', 'Rechazado'), ('P', 'Pendiente')], default='P', max_length=1, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='spacereservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spacereservation_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
