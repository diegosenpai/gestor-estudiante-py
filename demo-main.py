"""
Programa que permite registrar estudiantes y sus materias
El usuario registra el nombre de un estudiante y un listado de materias, con sus respectivas notas
Adicionalmente permite consultar el listado de estudiantes registrados.
Permite también consultar la información de un estudiante a partir de su nombre
También es posible consultar el promedio de un estudiante a partir de su nombre
"""
import os
import time
from estudiante import Estudiante
from nota import Nota

base_de_datos = []

"""
Lambda que permite borrar contenido de la pantalla
"""
clear = lambda: os.system('cls')


def agregar_estudiante (estudiante):
    base_de_datos.append(estudiante)

"""
Función que permite verificar si un estudiante
se encuentra registrado en la base de la aplicación.
Recibe como parametro el nombre a buscar.
retorna True si el existe un estudiante con ese nombre
o False si no existe registro de un estudiante con ese nombre
"""
def existeEstudianteEnBDD(nombreEstudiante):
    for item in base_de_datos:
        if item.getNombreEstudiante() == nombreEstudiante:
            return True
    return False

"""
Busca un estudiante por su nombre
Recibe como parametro una cadena que contiene el nombre del estudiante a buscar
retorna un diccionario que contiene como clave el nombre del estudiante y valor
una lista de tuplas. Cada tupla contiene el nombre de la materia y su nota.
"""
def buscarEstudiantePorNombre(nombreEstudiante):
    for item in base_de_datos:
        if item.getNombreEstudiante() == nombreEstudiante:
            return item

"""
Función que permite imprimir en pantalla la informacion del estudiante
Recibe como parametro un diccionario que representa el estudiante consultado
"""
def imprimirEstudiante(estudiante):
    print(estudiante)
    print(estudiante.imprimirNotas())
    print("acaba aqui")

"""
Función que permite calcular el promedio de un estudiante
Recibe como parametro el nombre del estudiante como una cadena de caracteres
Retorna un valor decimal que contiene el promedio calculado a partir de la
lista de tuplas de materias asociado al estudiante ingresado
"""
def obtenerPromedioPorEstudiante(nombreEstudiante):
    unEstudiante = buscarEstudiantePorNombre(nombreEstudiante)    
    return unEstudiante.obtenerPromedioEstudiante()

"""
Función utilitaria que permite ordenar la lista de estudiantes
definida como base de datos de la aplicación.
"""
def protoLambda (item):    
    return item.obtenerPromedioEstudiante()



def obtenerListaMaterias(listaMaterias,listaCalificaciones):
    contador = 0
    materias = []        
    for materia in listaMaterias:
        unaMateria = listaMaterias[contador]
        unaCalificacion = listaCalificaciones[contador]
        nota = Nota(unaMateria,unaCalificacion)
        materias.append(nota)
        contador = contador + 1
    return materias

"""
Función que permite imprimir el contenido de la lista de
diccionarios que cumple el objetivo de base de datos de la aplicación
"""
def imprimirContenido (baseAplicacion):
    for item in baseAplicacion:
        imprimirEstudiante(item)

while True:
    print("Bienvenido a Gestion de Estudiantes")
    print("1. Ingreso de Estudiante")
    print("2. Consultar Promedio por Estudiante")
    print("3. Imprimir Lista de Estudiantes")
    print("4. Mostrar Información de Estudiante")
    print("5. Salir")
    opcion = input("Ingrese su opción: ")
    if opcion.isdigit() :
        valorIngresado = int(opcion)
        if valorIngresado > 5:
            print(f"El texto ingresado {opcion} no es una opción válida. Regresando al menú principal")
            time.sleep(2)
            clear()
        elif valorIngresado == 1:
            clear()
            print(":::::Ingreso de Estudiante:::::")
            nombreEstudiante = input("Ingrese el nombre del estudiante. Presione 0 para salir.\n")
            materias = []
            notas = []
            while True:
                materia = input ("Ingrese el nombre de la materia: (Presione 0 para terminar de ingresar Materias)\n")
                if materia == "0":
                    break
                materias.append(materia)
            # loop notas
            for materia in materias:
                while True :
                    nota = input(f"Ingrese la nota  para la materia {materia}: \n")
                    if nota.isdigit() and float(nota) > 0:
                        valor = float(nota)
                        notas.append(valor)
                        break;
                    else:
                        print(f"El valor ingresado como nota:{nota} no correponde a una nota valida")
            asignaturas = obtenerListaMaterias(materias,notas)            
            unEstudiante = Estudiante(nombreEstudiante,asignaturas)
            agregar_estudiante(unEstudiante)
        elif valorIngresado == 2 :
            nombreIngresado = input("Ingrese el nombre del estudiante para calcular su promedio\n")
            if existeEstudianteEnBDD(nombreIngresado):
                promedioCalculado = obtenerPromedioPorEstudiante(nombreIngresado)
                print(f"El promedio para {nombreIngresado} es {promedioCalculado:.2f}")
            else:
                print(f"El nombre ingresado: {nombreIngresado} no se encuentra registrado")

        elif valorIngresado == 3:
            if len(base_de_datos) >0 :
                imprimirContenido(sorted(base_de_datos,key = protoLambda, reverse = True))
            else:
                print("No existen registros en la aplicación. Seleccione la opcíon 1 para registrar un estudiante.")
        elif valorIngresado == 4:
            nombreBuscar = input("Ingrese el nombre del estudiante a consultar: ")
            if existeEstudianteEnBDD(nombreBuscar):
                estudiante = buscarEstudiantePorNombre(nombreBuscar)
                imprimirEstudiante(estudiante)
                print("weirdo")
            else:
                print(f"El nombre ingresado:{nombreBuscar} no se encuentra registrado")
        elif valorIngresado == 5:
            print("Ha seleccionado salir...Hasta Luego")
            break
    else:
        print(f"El texto ingresado {opcion} no es una opción válida. Regresando al menú principal")
        time.sleep(2)
        clear()