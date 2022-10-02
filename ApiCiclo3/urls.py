from django.urls import path
from . import views
from .views import EmpresaViews

urlpatterns=[

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
    path('NuevoEmpleado/', views.NuevoEmpleado, name="NuevoEmpleado"),
    path('ConsultarEmpleado/', views.ConsultarEmpleado, name="ConsultarEmpleado"),
    path('EditarEmpleado/', views.EditarEmpleado, name="EditarEmpleado"),

    #Usuario
    path('NuevoUsuario/', views.NuevoUsuario, name="NuevoUsuario"),
    path('ConsultarUsuario/', views.ConsultarUsuario, name="ConsultarUsuario"),
    path('EditarUsuario/', views.EditarUsuario, name="EditarUsuario"),

    #Transacciones Admin
    path('NuevaTransaccion/', views.NuevaTransaccion, name="NuevaTransaccion"),
    path('ConsultarTransaccion/', views.ConsultarTransaccion, name="ConsultarTransaccion"),

    #Transacciones Emp
    path('NuevaTransaccionEm/', views.NuevaTransaccionEm, name="NuevaTransaccionEm"),
    path('ConsultarTransaccionEm/', views.ConsultarTransaccionEm, name="ConsultarTransaccionEm"),

    #Usuario US
    path('EditarUsuarioUS/', views.EditarUsuarioUS, name="EditarUsuarioUS")
]