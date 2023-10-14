
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

    def obtenerPromedioPorEstudiante(self,nombreEstudiante):
        unEstudiante = self.buscarEstudiantePorNombre(nombreEstudiante)    
        return unEstudiante.obtenerPromedioEstudiante()

    def existenRegistrosEnBase(self):
        if len(self.__baseDatos) >0:
            return True
        return False
    
   
    def obtenerBaseOrdenada(self):
        return sorted(self.__baseDatos,key=lambda e: e.obtenerPromedioEstudiante(),reverse=True)
