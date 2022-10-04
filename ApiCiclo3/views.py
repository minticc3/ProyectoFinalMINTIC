import json
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from ApiCiclo3.models import Empleado, Rol, Usuario, Empresa


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

################  EMPRESA #################
class EmpresaViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, ide=0):
        if(ide>0):
            emp = list(Empresa.objects.filter(id_empresa = ide).values())
            if(len(emp)>0):
                empRes = emp[0]
                data = {'Empresa=>':empRes}
            else:
                data = {'Empresas':"Objecto no encontrado"}
        else:
            template_name="Admin/Empresa/ConsultarEmpresa.html"
            emp = Empresa.objects.all()
            data = {'empresas':emp}
        return render(request, template_name, data)

    def post(self, request):
        template_name="Admin/Empresa/NuevaEmpresa.html"
        Empresa.objects.create(id_empresa = request.POST["id_empresa"],
                               nombre = request.POST["nombre"],
                               nit = request.POST["nit"],
                               ciudad = request.POST["ciudad"],
                               direccion = request.POST["direccion"],
                               fecha_creacion = request.POST["fecha_creacion"])
        return redirect('/Empresa/')

def NuevaEmpresa(request):
    return render(request, 'Admin/Empresa/NuevaEmpresa.html')

def EditarEmpresa(request, ide):
    emp = Empresa.objects.get(id_empresa = ide)
    data = {
        'empresa':emp
    }
    return render(request, 'Admin/Empresa/EditarEmpresa.html', data)

def updateEmpresa(request):
    id_empresa = request.POST['id_empresa']
    nombre = request.POST['nombre']
    nit = request.POST['nit']
    ciudad = request.POST['ciudad']
    direccion = request.POST['direccion']
    fecha_creacion = request.POST['fecha_creacion']
    emp = Empresa.objects.get(id_empresa = id_empresa)
    emp.nombre = nombre
    emp.nit = nit
    emp.ciudad = ciudad
    emp.direccion = direccion
    emp.fecha_creacion = fecha_creacion
    emp.save()
    return redirect('/Empresa/')

def EliminarEmpresa(request, ide):
    Empresa.objects.filter(id_empresa = ide).delete()
    return redirect('/Empresa/')

################ FIN EMPRESA ###############

################  EMPLEADO #################
class EmpleadoViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, idem=0):
        if(idem>0):
            empl = list(Empleado.objects.filter(id_empleado = idem).values())
            if(len(empl)>0):
                emplRes = empl[0]
                data = {'Empleado=>':emplRes}
            else:
                data = {'Empleado':"Objecto no encontrado"}
        else:
            template_name="Admin/Empleado/ConsultarEmpleado.html"
            empl = Empleado.objects.all()
            data = {'empleados':empl}
        return render(request, template_name, data)

    def post(self, request):
        template_name="Admin/Empleado/NuevoEmpleado.html"
        empresa = Empresa.objects.get(id_empresa = request.POST["id_empresa"])
        Empleado.objects.create(id_empleado = request.POST["id_empleado"],
                               nombre = request.POST["nombre"],
                               apellido = request.POST["apellido"],
                               email = request.POST["email"],
                               id_empresa = empresa,
                               fecha_creacion = request.POST["fecha_creacion"])
        return redirect('/Empleado/')

def NuevoEmpleado(request):
    return render(request, 'Admin/Empleado/NuevoEmpleado.html')   

def EditarEmpleado(request, idem):
    empl = Empleado.objects.get(id_empleado=idem)
    data ={
        'empleado':empl
    }
    return render(request, 'Admin/Empleado/EditarEmpleado.html', data)

def updateEmpleado(request):
        empresa = Empresa.objects.get(id_empresa = request.POST["id_empresa"])
        id_empleado = request.POST['id_empleado']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        id_empresa = empresa
        fecha_creacion = request.POST['fecha_creacion']
        empleado = Empleado.objects.get(id_empleado = id_empleado)
        empleado.nombre = nombre
        empleado.apellido = apellido
        empleado.email = email
        empleado.id_empresa = id_empresa
        empleado.fecha_creacion = fecha_creacion
        empleado.save()
        return redirect('/Empleado/')

def eliminarEmpleado(request, idem):
    Empleado.objects.filter(id_empleado = idem).delete()
    return redirect('/Empleado/')

### FIN EMPLEADO #########################

################  USUARIO #################

class UsuarioViews(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self,request,idem=0):
        if(idem>0):
            usu=list(Usuario.objects.filter(id_usuario=idem).values())
            if(len(usu)>0):
                usuRes=usu[0]
                data={'Usuario=>':usuRes}
            else:
                data={'Usuario=>':"Usuario no encontrado"}    
        else:
            template_name="Admin/Usuario/ConsultarUsuario.html"
            usu = Usuario.objects.all()
            data= {'usuario':usu}
        return render(request, template_name, data)    

    
    def post(self, request):
        template_name="Admin/Usuario/NuevoUsuario.html"
        empleado=Empleado.objects.get(id_empleado=request.POST["id_empleado"])
        rol=Rol.objects.get(id_rol=request.POST["id_rol"])
        Usuario.objects.create(id_usuario=request.POST["id_usuario"],
                              email=request.POST["email"],
                              imagen=request.POST["imagen"],
                              contrasena=request.POST["contrasena"],
                              id_rol=rol,
                              fecha_creacion=request.POST["fecha_creacion"],
                              id_empleado =empleado)
        return redirect('/Usuario/')    
                
def NuevoUsuario(request):
    return render(request, 'Admin/Usuario/NuevoUsuario.html')   

def EditarUsuario(request, idem):
    usu = Usuario.objects.get(id_usuario= idem)
    data ={'usuario': usu}
    return render(request, 'Admin/Usuario/EditarUsuario.html', data)



def updateUsuario(request):
    empleado=Empleado.objects.get(id_empleado=request.POST["id_empleado"])
    rol=Rol.objects.get(id_rol=request.POST["id_rol"])
    id_usuario=request.POST["id_usuario"]
    email=request.POST["email"]
    imagen=request.POST["imagen"]
    contrasena=request.POST["contrasena"]
    id_rol=rol
    fecha_creacion=request.POST["fecha_creacion"]
    id_empleado =empleado
    usuario=Usuario.objects.get(id_usuario=request.POST["id_usuario"])
    usuario.email = email
    usuario.imagen = imagen
    usuario.contrasena = contrasena
    usuario.id_rol = id_rol
    usuario.fecha_creacion = fecha_creacion
    usuario.id_empleado = id_empleado
    usuario.save()
    return redirect('/Usuario/')


def eliminarUsuario(request, idem):    
    Usuario.objects.filter(id_usuario=idem).delete()
    return redirect('/Usuario/')
    
### FIN USUARIO #########################


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
