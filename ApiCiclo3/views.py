from django.shortcuts import render

from ApiCiclo3.models import Empleado, Usuario

# Create your views here.

def loginUser(request):
    if(request.method=='POST'):
        try:
            UserValidation = Usuario.objects.get(email=request.POST['email'],contrasena=request.POST['contrasena'])
            if(UserValidation.id_rol.id_rol==1):
                request.session['email']=UserValidation.email
                return  render(request, 'Admin/welcome.html')
            elif(UserValidation.id_rol.id_rol==2):
                request.session['email']=UserValidation.email
                return  render(request, 'Empleado/welcome.html')
            elif(UserValidation.id_rol.id_rol==3):
                request.session['email']=UserValidation.email
                return  render(request, 'Usuario/welcome.html')                
        except Usuario.DoesNotExist:
            return render(request, 'login/login.html')
            #message.warning(request, "Usuario o Contraseña Incorrectos")
    return render(request, 'login/login.html')

def NuevaEmpresa(request):
    return render(request, 'Admin/Empresa/NuevaEmpresa.html')   

def ConsultarEmpresa(request):
    return render(request, 'Admin/Empresa/ConsultarEmpresa.html')      

def EditarEmpresa(request):
    return render(request, 'Admin/Empresa/EditarEmpresa.html')    

def NuevoEmpleado(request):
    return render(request, 'Admin/Empleado/NuevoEmpleado.html')   

def ConsultarEmpleado(request):
    return render(request, 'Admin/Empleado/ConsultarEmpleado.html')      

def EditarEmpleado(request):
    return render(request, 'Admin/Empleado/EditarEmpleado.html') 

def NuevoUsuario(request):
    return render(request, 'Admin/Usuario/NuevoUsuario.html')   

def ConsultarUsuario(request):
    return render(request, 'Admin/Usuario/ConsultarUsuario.html')      

def EditarUsuario(request):
    return render(request, 'Admin/Usuario/EditarUsuario.html')     

def NuevaTransaccion(request):
    return render(request, 'Admin/Transacciones/NuevaTransaccion.html')   

def ConsultarTransaccion(request):
    return render(request, 'Admin/Transacciones/ConsultarTransaccion.html')   

def NuevaTransaccionEm(request):
    return render(request, 'Empleado/Transacciones/NuevaTransaccionEm.html')   

def ConsultarTransaccionEm(request):
    return render(request, 'Empleado/Transacciones/ConsultarTransaccionEm.html')   

def EditarUsuarioUS(request):
    return render(request, 'Usuario/EditarUsuarioUS.html')   
