class Nota :
    def __init__(self,nombreMateria,valor):
        self.__nombreMateria = nombreMateria
        self.__valor = valor
    
    def getNombreMateria(self):
        return self.__materia
    
    def getValorNota(self):
        return self.__valor