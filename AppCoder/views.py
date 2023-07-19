from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso, Profesor, Entregable, Estudiante
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EntregableFormulario

# Create your views here.
def curso(self):
    curso = Curso(nombre='Desarrollo Web', camada='19881')

    documentodeTexto = f'---->Curso: {curso.nombre} Camada: {curso.camada}'

    return HttpResponse(documentodeTexto)

def entregable(self):
    entregable = Entregable(nombre='Desarrollo Web', camada='19881')

    documentodeTexto = f'---->Entregable: {entregable.nombre} Fecha de Entrega: {entregable.fecha_entrega}'

    return HttpResponse(documentodeTexto)

def profesores(self):
    profesores = Profesor(nombre='Desarrollo Web', camada='19881')

    documentodeTexto = f'---->Profesores: {profesores.nombre} Apellido: {profesores.apellido} Email: {profesores.email} Profesion: {profesores.profesion}'

    return HttpResponse(documentodeTexto)

def estudiantes(self):
    estudiantes = Estudiante(nombre='Desarrollo Web', camada='19881')

    documentodeTexto = f'---->Profesores: {estudiantes.nombre} Apellido: {estudiantes.apellido} Email: {estudiantes.email}' 

    return HttpResponse(documentodeTexto)


def inicio(request):
    return render(request, 'inicio.html')


def cursos(request):
 
      if request.method == "POST":
 
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], 
                                camada=informacion["camada"])
                  curso.save()
                  return render(request, "inicio.html")
      else:
            miFormulario = CursoFormulario()
 
      return render(request, "cursos.html", {"miFormulario": miFormulario})




def profesores(request):
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], 
                                apellido=informacion['apellido'],
                                email=informacion['email'],
                                profesion=informacion['profesion'])
            profesor.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = ProfesorFormulario()

    return render(request, 'profesores.html', {'miFormulario': miFormulario})



def entregables(request):
    if request.method == "POST":
        miFormulario = EntregableFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            entregables = Entregable(nombre=informacion['nombre'], 
                                    fecha=informacion['fecha'])
            entregable.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = EntregableFormulario()

    return render(request, 'entregables.html', {'miFormulario': miFormulario})



def busquedaCamada(request):
     return render(request, 'busquedaCamada.html')

def buscar(request):

    if request.GET['camada']:
          
        #respuesta = f"Estoy buscando la Camada nro.: {request.GET['camada']}"
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, 'inicio.html', {'cursos':cursos, 'camada':camada})
     
    else:
        respuesta = "No se han enviado datos."

    #return HttpResponse(respuesta)
    return render(request, 'inicio.html', {'respuesta':respuesta})


def buscar_curso(request):

    if request.GET['camada']:
          
        #respuesta = f"Estoy buscando la Camada nro.: {request.GET['camada']}"
        
        nombre = request.GET['nombre']
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada, nombre__icontains=nombre)        
        
        return render(request, 'inicio.html', {'cursos':cursos, 'camada':camada})
     
    else:
        respuesta = "No se han enviado datos."

    #return HttpResponse(respuesta)
    return render(request, 'inicio.html', {'respuesta':respuesta})


def buscar_profesor(request):

    if request.GET['email']:
        
        nombre = request.GET['nombre']
        apellido = request.GET['apellido']
        email = request.GET['email']
        profesion = request.GET['profesion']

        profesores = Profesor.objects.filter(nombre__icontains=nombre, apellido__icontains=apellido, email__icontains=email, profesion__icontains=profesion)        
        
        return render(request, 'inicio.html', {'nombre':nombre, 'apellido':apellido, 'email':email, 'profesion':profesion})
     
    else:
        respuesta = "No se han enviado datos."

    #return HttpResponse(respuesta)
    return render(request, 'inicio.html', {'respuesta':respuesta})


def buscar_entregable(request):

    if request.GET['nombre']:
        
        nombre = request.GET['nombre']
        fecha = request.GET['fecha']
       
        entregables = Entregable.objects.filter(nombre__icontains=nombre, fecha__icontains=fecha)        
        
        return render(request, 'inicio.html', {'nombre':nombre, 'fecha':fecha})
     
    else:
        respuesta = "No se han enviado datos."

    #return HttpResponse(respuesta)
    return render(request, 'inicio.html', {'respuesta':respuesta})


def buscar_estudiante(request):

    if request.GET['email']:
        
        nombre = request.GET['nombre']
        apellido = request.GET['apellido']
        email = request.GET['email']

        estudiantes = Estudiante.objects.filter(nombre__icontains=nombre, apellido__icontains=apellido, email__icontains=email)        
        
        return render(request, 'inicio.html', {'nombre':nombre, 'apellido':apellido, 'email':email})
     
    else:
        respuesta = "No se han enviado datos."

    #return HttpResponse(respuesta)
    return render(request, 'inicio.html', {'respuesta':respuesta})

