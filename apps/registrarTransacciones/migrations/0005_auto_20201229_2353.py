# Generated by Django 3.1.4 on 2020-12-30 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrarTransacciones', '0004_auto_20201229_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrarTransacciones.localidad'),
        ),
    ]
