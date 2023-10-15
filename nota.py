class Nota :
    def __init__(self,nombreMateria,valor):
        """
            Constructor de la clase Nota.
            Forma parte de un estaudiante. Un estudiante
            puede tener una lista de notas
        Args:
            nombreMateria string: nombre de la asignatura
            valor float: valor de la asignatura
        """
        self.__nombreMateria = nombreMateria
        self.__valor = valor
    
    def getNombreMateria(self):
        return self.__nombreMateria
    
    def getValorNota(self):
        return self.__valor