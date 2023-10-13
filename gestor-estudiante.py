
class GestorEstudiante():

    def __init__(self,baseDatos) :
        self.__baseDatos = baseDatos

    def agregarEstudianteABase(self,estudiante):
        self.__baseDatos.append(estudiante)

    
    def existeEstudianteEnBDD(self,nombreEstudiante):
        for item in self.__baseDatos:
            if item.getNombreEstudiante() == nombreEstudiante:
                return True
        return False
    
    def buscarEstudiantePorNombre(self,nombreEstudiante):
        for item in self.__baseDatos:
            if item.getNombreEstudiante() == nombreEstudiante:
                return item

    def imprimirEstudiante(estudiante):
        print(estudiante)
        estudiante.imprimirNotas()

    def obtenerPromedioPorEstudiante(self,nombreEstudiante):
        unEstudiante = self.buscarEstudiantePorNombre(nombreEstudiante)    
        return unEstudiante.obtenerPromedioEstudiante()
