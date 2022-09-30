from django.db import models

# Create your models here.
class Empresa(models.Model):
    id_empresa = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    nit = models.CharField(max_length=15)
    ciudad = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    fecha_creacion = models.DateField()

class Empleado(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido =  models.CharField(max_length=30)
    email =  models.CharField(max_length=50,unique=True)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fecha_creacion = models.DateField()

class Rol(models.Model): #Realizado en grupo
    id_rol = models.IntegerField(primary_key=True)
    nombre_rol = models.CharField(max_length=20, default="Administrador")

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=50,unique=True)
    imagen = models.CharField(max_length=80)
    contrasena = models.CharField(max_length=50)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    fecha_creacion = models.DateField()
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

class Transaccion(models.Model):
    id_transaccion = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    concepto = models.CharField(max_length=80)
    monto = models.FloatField(max_length=10)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo_transaccion=models.CharField(max_length=15, default='Egreso')
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)