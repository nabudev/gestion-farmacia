# Generated by Django 5.0.6 on 2024-05-27 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_cliente_telefono_medicamento_cantidad_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CuentaParticulare',
            new_name='CuentaParticular',
        ),
        migrations.RenameModel(
            old_name='MarcaComerciale',
            new_name='MarcaComercial',
        ),
        migrations.RenameModel(
            old_name='ObraSociale',
            new_name='ObraSocial',
        ),
        migrations.RenameModel(
            old_name='Proveedore',
            new_name='Proveedor',
        ),
        migrations.RenameModel(
            old_name='StockProveedore',
            new_name='StockProveedor',
        ),
    ]
