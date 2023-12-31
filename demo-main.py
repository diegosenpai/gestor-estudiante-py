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
from gestor import GestorEstudiante


"""
Lambda que permite borrar contenido de la pantalla
"""
clear = lambda: os.system('cls')

gestorEstudiante = GestorEstudiante([])



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

def imprimirEstudiante(estudiante):
    print(estudiante)
    estudiante.imprimirNotas()

"""
Función que permite imprimir el contenido de la lista de
diccionarios que cumple el objetivo de base de datos de la aplicación
"""
def imprimirContenido (baseAplicacion):
    for item in baseAplicacion:
        imprimirEstudiante(item)

def imprimirEstudiante(estudiante):
        print(estudiante)
        estudiante.imprimirNotas()

while True:
    print("Bienvenido a Gestion de Estudiantes")
    print("1. Ingreso de Estudiante")
    print("2. Consultar Promedio por Estudiante")
    print("3. Imprimir Lista de Estudiantes")
    print("4. Mostrar Información de Estudiante")
    print("5. Salir")
    opcion = input("Ingrese su opción: ")
    try :
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
                    try :
                        valor = float(nota)
                        notas.append(valor)
                        break;
                    except ValueError:
                        print(f"El valor ingresado como nota:{nota} no correponde a una nota valida")
            if gestorEstudiante.existeEstudianteEnBDD(nombreEstudiante) :
                print(f"El estudiante {nombreEstudiante} ya se encuentra registrado")
            else:
                asignaturas = obtenerListaMaterias(materias,notas)            
                unEstudiante = Estudiante(nombreEstudiante,asignaturas)
                gestorEstudiante.agregarEstudianteABase(unEstudiante)
        elif valorIngresado == 2 :
            nombreIngresado = input("Ingrese el nombre del estudiante para calcular su promedio\n")
            if gestorEstudiante.existeEstudianteEnBDD(nombreIngresado):
                promedioCalculado = gestorEstudiante.obtenerPromedioPorEstudiante(nombreIngresado)
                print(f"El promedio para {nombreIngresado} es {promedioCalculado:.2f}")
            else:
                print(f"El nombre ingresado: {nombreIngresado} no se encuentra registrado")

        elif valorIngresado == 3:
            if gestorEstudiante.existenRegistrosEnBase() :
                imprimirContenido(gestorEstudiante.obtenerBaseOrdenada())
            else:
                print("No existen registros en la aplicación. Seleccione la opcíon 1 para registrar un estudiante.")
        elif valorIngresado == 4:
            nombreBuscar = input("Ingrese el nombre del estudiante a consultar: ")
            if gestorEstudiante.existeEstudianteEnBDD(nombreBuscar):
                estudiante = gestorEstudiante.buscarEstudiantePorNombre(nombreBuscar)
                imprimirEstudiante(estudiante)
            else:
                print(f"El nombre ingresado:{nombreBuscar} no se encuentra registrado")
        elif valorIngresado == 5:
            print("Ha seleccionado salir...Hasta Luego")
            break
    except ValueError:
        print(f"El texto ingresado {opcion} no es una opción válida. Regresando al menú principal")
        time.sleep(2)
        clear()