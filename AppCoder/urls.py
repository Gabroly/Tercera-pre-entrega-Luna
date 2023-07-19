from django.urls import path
from AppCoder import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    path('busquedaCamada', views.busquedaCamada, name='BusquedaCamada'),
    #path('entregableFormulario', views.entregableFormulario, name="EntregableFormulario"),
    path('buscar/', views.buscar),
    path('buscar_curso/', views.buscar_curso),
    path('buscar_profesor/', views.buscar_profesor),
    path('buscar_entregable/', views.buscar_entregable),
    path('busacar_estudiante/', views.buscar_estudiante),

]
