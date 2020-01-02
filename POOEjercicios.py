
class Vehiculo():
    def __init__(self,color,ruedas):
        self.__color=color
        self.__ruedas=ruedas

    def __str__(self):
        return "Color {}, {}  reudas, ". format(self.__color,self.__ruedas)

class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindrada ):
        Vehiculo.__init__(self,color,ruedas)
        self.__velocidad=velocidad
        self.__cilindrada=cilindrada
    def __str__(self):
        return  Vehiculo.__str__(self)+" {}  km/h, {} cc ". format(self.__velocidad,self.__cilindrada)

micoche=Coche("azul", 4,150,1200)
print(micoche)