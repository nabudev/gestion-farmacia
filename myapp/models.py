from django.db import models

# Create your models here.
class ObraSocial(models.Model):
    nombre= models.CharField(max_length=45)
    descuento= models.IntegerField(null=True)
    
    def __str__(self):
        return self.nombre
    
class MetodoPago(models.Model):
    metodo= models.CharField(max_length=10)
    
class Cliente (models.Model):
    dni= models.IntegerField(primary_key=True)
    apellido= models.CharField(max_length=45)
    nombre= models.CharField(max_length=45)
    domicilio= models.CharField(max_length=30)
    telefono= models.IntegerField(null=True)
    obra_social= models.ForeignKey(ObraSocial, on_delete=models.CASCADE)
    
class CuentaParticular(models.Model):
    cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    saldo= models.CharField(max_length=15)
    
class Laboratorio(models.Model):
    nombre= models.CharField(max_length=45)
    
class CompuestoGenerico(models.Model):
    nombre= models.CharField(max_length=45)
    
class MarcaComercial(models.Model):
    nombre= models.CharField(max_length=45)
    
class PresentacionMedicamento(models.Model):
    tipo= models.CharField(max_length=25)

class Medicamento(models.Model):
    marca_comercial= models.ForeignKey(MarcaComercial, on_delete=models.CASCADE)
    compuesto_generico= models.ForeignKey(CompuestoGenerico, on_delete=models.CASCADE)
    presentacion_medicamento= models.ForeignKey(PresentacionMedicamento, on_delete=models.CASCADE)
    dosificacion= models.CharField(max_length=25)
    cantidad= models.IntegerField(null=True)
    laboratorio= models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    
class Proveedor(models.Model):
    apellido= models.CharField(max_length=45)
    nombre= models.CharField(max_length=45)
    telefono= models.IntegerField(null=True)
    direccion= models.CharField(max_length=30)
    
class StockProveedor(models.Model):
    proveedor= models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    medicamento= models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    
class Venta(models.Model):
    cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    metodo_pago= models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    medicamento= models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad= models.IntegerField(null=True)
    precio_unitario= models.IntegerField(null=True)
    precio_total= models.IntegerField(null=True)
    
    