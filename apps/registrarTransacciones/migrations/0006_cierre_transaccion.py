# Generated by Django 3.1.4 on 2020-12-30 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrarTransacciones', '0005_auto_20201229_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cierre',
            fields=[
                ('id_cierre', models.AutoField(primary_key=True, serialize=False)),
                ('valor', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_alta', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cierre',
                'verbose_name_plural': 'Cierres',
                'ordering': ['fecha_alta'],
            },
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id_transaccion', models.AutoField(primary_key=True, serialize=False)),
                ('valor', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_alta', models.DateField(auto_now=True)),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registrarTransacciones.cliente')),
            ],
            options={
                'verbose_name': 'Transaccion',
                'verbose_name_plural': 'Transacciones',
                'ordering': ['id_transaccion'],
            },
        ),
    ]