class Estudiante:
    def __init__(self,nombreEstudiante,calificaciones):
        """_summary_
            Constructor de la clase Estudiante
        Args:
            nombreEstudiante (String): nombre del estudiante
            calificaciones (Nota): lista de objetos Nota
        """
        self.__nombreEstudiante = nombreEstudiante
        self.__calificaciones = calificaciones
    
    def obtenerPromedioEstudiante(self):
        """
            Retorna promedio del estudiante, obtenido a partir del 
            listado de notas 
        Returns:
            decimal: promedio del estudiante
        """
        if len(self.__calificaciones) == 0:
            return 0
        else:
            items = len(self.__calificaciones)
            total = 0
            for item in self.__calificaciones:
                total += item.getValorNota()
            return total / items
    
    def getNombreEstudiante(self):
        """
        Retorna el nombre del estudiante

        Returns:
            String: nombre del estudiante
        """
        return self.__nombreEstudiante
    
    def getCalificacionesEstudiante(self):
        """
            Retorna el listado de notas del estudiante
        Returns:
            Iterable Nota: lista de notas del estudiante
        """
        return self.__calificaciones
    
    def imprimirNotas(self):
        """Imprime en consola contenido de notas del estudiante
        """
        print("+++++++ Materias")
        for nota in self.__calificaciones:
            print(f"+++++++++++ Materia: {nota.getNombreMateria()}, Calificacion: {nota.getValorNota():.2f}")
    
    def __str__(self) :
        """_summary_
        Retorna el nombre del estudiante y su promedio como string
        Returns:
            string: contenido del objeto estudiante como string
        """
        msg = "Nombre Estudiante: {0} promedio {1:.2f}"
        return msg.format(self.__nombreEstudiante,self.obtenerPromedioEstudiante())
