from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from ApiCiclo3.models import Empleado, Usuario, Empresa


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


### FIN EMPRESA #########################
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
