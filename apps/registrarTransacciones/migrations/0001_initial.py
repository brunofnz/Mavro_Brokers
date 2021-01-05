# Generated by Django 3.1.4 on 2020-12-29 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('localidad', models.CharField(max_length=50, null=True)),
                ('telefono', models.CharField(max_length=50, null=True)),
                ('mail', models.CharField(max_length=50, null=True)),
                ('fecha_alta', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id_transaccion', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registrarTransacciones.usuario')),
            ],
            options={
                'verbose_name': 'Transaccion',
                'verbose_name_plural': 'Transacciones',
                'ordering': ['id_transaccion'],
            },
        ),
    ]