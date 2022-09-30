from django.contrib import admin
from .models import Empresa,Empleado,Usuario,Rol,Transaccion

admin.site.register(Empresa)
admin.site.register(Empleado)
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Transaccion)

