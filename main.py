from nota import Nota
from estudiante import Estudiante

mate = Nota("Mate",15)
lengua = Nota("Lengua",20)
lab = Nota("Lab",17)
science = Nota("Science",18)
calificaciones = [mate,lengua]
otrasCalificaciones = [lab,science,mate]
diego = Estudiante("Diego",calificaciones)
emi = Estudiante("Emi",otrasCalificaciones)
base_de_datos = [emi,diego]
print(diego.obtenerPromedioEstudiante())
print(emi.obtenerPromedioEstudiante())
for item in base_de_datos:
    print(item)
print("Luego de ordenar")
ordenada = sorted(base_de_datos,key=lambda e : e.obtenerPromedioEstudiante(),reverse=True)
for item in ordenada:
    print(item)