from django.urls import path
from . import views
from .views import EmpresaViews, EmpleadoViews, TransaccionViews, UsuarioViews


urlpatterns=[
    # path('/', views.index, name="index"),
    #Login
    path('login/',views.loginUser, name="Login"),

    #Empresa
    path('Empresa/', EmpresaViews.as_view(), name="Listar-Nuevo"),
    path('Empresa/<int:ide>', EmpresaViews.as_view(), name="Eliminar-Actualizar"),
    path('NuevaEmpresa/', views.NuevaEmpresa, name="NuevaEmpresaForm"),
    path('EditarEmpresa/<int:ide>', views.EditarEmpresa, name="EditarEmpresaForm"),
    path('updateEmpresa/', views.updateEmpresa, name="EditarEmpresa"),
    path('EliminarEmpresa/<int:ide>', views.EliminarEmpresa, name="Eliminar"),

    #Empleado
    path('Empleado/', EmpleadoViews.as_view(), name="Listar-Nuevo"),
    path('Empleado/<int:idem>', EmpleadoViews.as_view(), name="Eliminar-Actualizar"),
    path('NuevoEmpleado/', views.NuevoEmpleado, name="NuevoEmpleado"),
    path('EditarEmpleado/<int:idem>', views.EditarEmpleado, name="EditarEmpleado"),
    path('updateEmpleado/', views.updateEmpleado, name="EditarEmpleado"),
    path('EliminarEmpleado/<int:idem>', views.eliminarEmpleado, name="Eliminar"),

    #Usuario
    path('Usuario/', UsuarioViews.as_view(), name="Lista-Nuevo"),
    path('Usuario/<int:idem>', UsuarioViews.as_view(), name="Eliminar-Actualizar"),
    path('NuevoUsuario/', views.NuevoUsuario, name="NuevoUsuario"),
    path('EditarUsuario/<int:idem>', views.EditarUsuario, name="EditarUsuario"),
    path('updateUsuario/', views.updateUsuario, name="EditarUsiario"),
    path('EliminarUsuario/<int:idem>', views.eliminarUsuario, name="Eliminar"),

    #Transacciones
    path('Transaccion/', TransaccionViews.as_view(), name="Listar-Nuevo"),
    path('NuevaTransaccion/', views.NuevaTransaccion, name="NuevaTransaccion"),
    path('ConsultarTransaccion/', views.ConsultarTransaccion, name="ConsultarTransaccion"),
    path('NuevaTransaccionEm/', views.NuevaTransaccionEm, name="Nueva Empleado"),
    path('Admin/Transaccion/ConsultarTransaccion/', views.ConsultarTransaccion, name="ConsultarTransaccionAdmin"),

    #Usuario US
    path('UsuarioUs/<int:idem>', views.home, name="home"),
    path('EditarUsuarioUS/<int:idem>', views.EditarUsuarioUS, name="EditarUsuarioUS")
]