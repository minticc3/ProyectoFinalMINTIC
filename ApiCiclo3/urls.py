from django.urls import path
from . import views

urlpatterns=[

    #Login
    path('login/',views.loginUser, name="Login"),

    #Empresa
    path('NuevaEmpresa/', views.NuevaEmpresa, name="NuevaEmpresa"),
    path('ConsultarEmpresa/', views.ConsultarEmpresa, name="ConsultarEmpresa"),
    path('EditarEmpresa/', views.EditarEmpresa, name="EditarEmpresa"),

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