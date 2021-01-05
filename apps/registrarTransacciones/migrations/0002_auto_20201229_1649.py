# Generated by Django 3.1.4 on 2020-12-29 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrarTransacciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaccion',
            name='fecha_alta',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='tipo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='valor',
            field=models.CharField(max_length=50, null=True),
        ),
    ]