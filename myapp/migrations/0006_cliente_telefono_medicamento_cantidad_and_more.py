# Generated by Django 5.0.6 on 2024-05-27 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_obrasocial_obrasociale'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='medicamento',
            name='cantidad',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='obrasociale',
            name='descuento',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='proveedore',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='cantidad',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='precio_total',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='precio_unitario',
            field=models.IntegerField(null=True),
        ),
    ]