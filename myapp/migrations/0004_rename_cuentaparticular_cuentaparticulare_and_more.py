# Generated by Django 5.0.6 on 2024-05-27 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_ventas_venta'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CuentaParticular',
            new_name='CuentaParticulare',
        ),
        migrations.RenameModel(
            old_name='MarcaComercial',
            new_name='MarcaComerciale',
        ),
        migrations.RenameModel(
            old_name='Proveedor',
            new_name='Proveedore',
        ),
        migrations.RenameModel(
            old_name='StockProveedor',
            new_name='StockProveedore',
        ),
    ]