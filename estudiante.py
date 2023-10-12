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
    
    def __str__(self) :
        msg = "nombre estudiante {0} promedio {1}"
        return msg.format(self.__nombreEstudiante,self.obtenerPromedioEstudiante())
