
class GestorEstudiante():

    def __init__(self,baseDatos) :
        """Constructor de la clase GestorEstudiante
            Permite gestionar la base de datos de estudiantes.
            Recibe como parametro la lista de estudiantes a la
            que se pueden ir agregando estudiantes.
        Args:
            baseDatos iterable: lista de estudiantes
        """
        self.__baseDatos = baseDatos

    def agregarEstudianteABase(self,estudiante):
        """
            Funcion que permite agregar un estudiante a la 
            base de estudiantes
        Args:
            estudiante Estudiante: elemento a ingresar a la base
        """
        self.__baseDatos.append(estudiante)

    
    def existeEstudianteEnBDD(self,nombreEstudiante):
        """
            Funcion que verifica si un estudiante se encuentra
            en la base de estudiantes, a partir de su nombre.
        Args:
            nombreEstudiante string : Nombre del estudiante a buscar

        Returns:
            boolean: True en el caso de que el estudiante se encuentre registrado en la base,
                        False en el caso contrario.
        """
        for item in self.__baseDatos:
            if item.getNombreEstudiante() == nombreEstudiante:
                return True
        return False
    
    def buscarEstudiantePorNombre(self,nombreEstudiante):
        """
            Funcion que permite buscar un estudiante en la base de estudiantes
            a partir del nombre del estudiante
        Args:
            nombreEstudiante string: nombre del estudiante a buscar

        Returns:
            Estudiante: estudiante que tiene el atributo nombreEstudiante igual al nombre 
                        ingresado como argumento
        """
        for item in self.__baseDatos:
            if item.getNombreEstudiante() == nombreEstudiante:
                return item

    def obtenerPromedioPorEstudiante(self,nombreEstudiante):
        """
            Retorna el promedio del estudiante que coincide con el nombre del estudiante
            ingresado.
        Args:
            nombreEstudiante (string): nombre del estudiante a buscar

        Returns:
            float: promedio del estudiante que tiene el atributo nombreEstudiante igual al 
                    argumento.
        """
        unEstudiante = self.buscarEstudiantePorNombre(nombreEstudiante)    
        return unEstudiante.obtenerPromedioEstudiante()

    def existenRegistrosEnBase(self):
        """Verifica si existen registros de estudiantes en la base de estudiantes

        Returns:
            boolean: retorna True si al menos existe un registro en la base de estudiantes.
        """
        if len(self.__baseDatos) >0:
            return True
        return False
    
   
    def obtenerBaseOrdenada(self):
        return sorted(self.__baseDatos,key=lambda e: e.obtenerPromedioEstudiante(),reverse=True)
