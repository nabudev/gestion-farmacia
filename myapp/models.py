from django.db import models

# Create your models here.
class ObraSociale(models.Model):
    nombre= models.CharField(max_length=45)
    descuento= models.IntegerField
    
class MetodoPago(models.Model):
    metodo= models.CharField(max_length=10)
    
class Cliente (models.Model):
    dni= models.IntegerField(primary_key=True)
    apellido= models.CharField(max_length=45)
    nombre= models.CharField(max_length=45)
    domicilio= models.CharField(max_length=30)
    telefono= models.IntegerField
    obra_social= models.ForeignKey(ObraSociale, on_delete=models.CASCADE)
    
class CuentaParticulare(models.Model):
    cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    saldo= models.CharField(max_length=15)
    
class Laboratorio(models.Model):
    nombre= models.CharField(max_length=45)
    
class CompuestoGenerico(models.Model):
    nombre= models.CharField(max_length=45)
    
class MarcaComerciale(models.Model):
    nombre= models.CharField(max_length=45)
    
class PresentacionMedicamento(models.Model):
    tipo= models.CharField(max_length=25)

class Medicamento(models.Model):
    marca_comercial= models.ForeignKey(MarcaComerciale, on_delete=models.CASCADE)
    compuesto_generico= models.ForeignKey(CompuestoGenerico, on_delete=models.CASCADE)
    presentacion_medicamento= models.ForeignKey(PresentacionMedicamento, on_delete=models.CASCADE)
    dosificacion= models.CharField(max_length=25)
    cantidad= models.IntegerField
    laboratorio= models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    
class Proveedore(models.Model):
    apellido= models.CharField(max_length=45)
    nombre= models.CharField(max_length=45)
    telefono= models.IntegerField
    direccion= models.CharField(max_length=30)
    
class StockProveedore(models.Model):
    proveedor= models.ForeignKey(Proveedore, on_delete=models.CASCADE)
    medicamento= models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    
class Venta(models.Model):
    cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    metodo_pago= models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    medicamento= models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad= models.IntegerField
    precio_unitario= models.IntegerField
    precio_total= models.IntegerField
    
    