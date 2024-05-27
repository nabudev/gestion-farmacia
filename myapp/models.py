from django.db import models

# Create your models here.
class ObraSocial(models.Model):
    nombre= models.CharField(max_length=45)
    descuento= models.IntegerField(null=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Obras Sociales"
    
class MetodoPago(models.Model):
    metodo= models.CharField(max_length=30)
    
    def __str__(self):
        return self.metodo
    
    class Meta:
        verbose_name_plural = "Metodos de pago"
    
class Cliente (models.Model):
    dni= models.IntegerField(primary_key=True)
    apellido= models.CharField(max_length=45)
    nombre= models.CharField(max_length=45)
    domicilio= models.CharField(max_length=30)
    telefono= models.IntegerField(null=True)
    obra_social= models.ForeignKey(ObraSocial, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__ (self):
        return f'{self.apellido} {self.nombre}'
    
class CuentaParticular(models.Model):
    cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    saldo= models.IntegerField(null=True, blank=True)
    
    def __str__ (self):
        return f'Titular: {self.cliente}, Saldo: {self.saldo}'
    
    class Meta:
        verbose_name_plural = "Cuentas Particulares"
    
class Laboratorio(models.Model):
    nombre= models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre
    
class CompuestoGenerico(models.Model):
    nombre= models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Compuestos Genericos"
    
class MarcaComercial(models.Model):
    nombre= models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Marcas Comerciales"
    
class PresentacionMedicamento(models.Model):
    tipo= models.CharField(max_length=25)
    
    def __str__(self):
        return self.tipo
    
    class Meta:
        verbose_name_plural = "Presentacion del medicamento"

class Medicamento(models.Model):
    marca_comercial= models.ForeignKey(MarcaComercial, on_delete=models.CASCADE)
    compuesto_generico= models.ForeignKey(CompuestoGenerico, on_delete=models.CASCADE)
    presentacion_medicamento= models.ForeignKey(PresentacionMedicamento, on_delete=models.CASCADE)
    dosificacion= models.CharField(max_length=25)
    cantidad= models.IntegerField(null=True)
    laboratorio= models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.marca_comercial} - {self.compuesto_generico} - {self.presentacion_medicamento} - {self.dosificacion}'
    
class Proveedor(models.Model):
    apellido= models.CharField(max_length=45)
    nombre= models.CharField(max_length=45)
    telefono= models.IntegerField(null=True)
    direccion= models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - Telefono: {self.telefono}'
    
    class Meta:
        verbose_name_plural = "Proveedores"
    
class StockProveedor(models.Model):
    proveedor= models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    medicamento= models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.proveedor} - {self.medicamento}'
    
    class Meta:
        verbose_name_plural = "Stock de proveedores"
    
class Venta(models.Model):
    cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    metodo_pago= models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    medicamento= models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad= models.IntegerField(null=True)
    precio_unitario= models.IntegerField(null=True)
    precio_total= models.IntegerField(null=True)
    
    def __str__(self):
        return f'{self.medicamento} - Cantidad: {self.cantidad} - Total: {self.precio_total}'
    
    