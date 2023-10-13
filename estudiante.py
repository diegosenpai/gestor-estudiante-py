class Estudiante:
    def __init__(self,nombreEstudiante,calificaciones):
        self.__nombreEstudiante = nombreEstudiante
        self.__calificaciones = calificaciones
    
    def obtenerPromedioEstudiante(self):
        if len(self.__calificaciones) == 0:
            return 0
        else:
            items = len(self.__calificaciones)
            total = 0
            for item in self.__calificaciones:
                total += item.getValorNota()
            return total / items
    
    def getNombreEstudiante(self):
        return self.__nombreEstudiante
    
    def getCalificacionesEstudiante(self):
        return self.__calificaciones
    
    def imprimirNotas(self):
        print("+++++++ Materias")
        for nota in self.__calificaciones:
            print(f"+++++++++++ Materia: {nota.getNombreMateria()} Calificacion: {nota.getValorNota():.2f}")
    
    def __str__(self) :
        msg = "Nombre Estudiante: {0} promedio {1:.2f}"
        return msg.format(self.__nombreEstudiante,self.obtenerPromedioEstudiante())
