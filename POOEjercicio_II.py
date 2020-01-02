
class Vehiculo():
    def __init__(self,color,ruedas):
        self.__color=color
        self.__ruedas=ruedas
    def __str__(self):
        return "Color {}, ruedad {}, ".format(self.__color,self.__ruedas)



class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindrada):
        Vehiculo.__init__(self,color,ruedas)
        self.__velocidad=velocidad
        self.__cilindrada=cilindrada
    def __str__(self):
        return Vehiculo.__str__(self)+"Velocidad {} Km/h, CC {} ".format(self.__velocidad, self.__cilindrada)


class Bicicleta(Vehiculo):
    def __init__(self,color,ruedad,tipo):
        Vehiculo.__init__(self,color,ruedad)
        self.__tipo=tipo
    def __str__(self):
        return Vehiculo.__str__(self)+" Tipo {} ".format(self.__tipo)
    
micoche=Coche("Rojo", 4,500,1200)
print(micoche)
miBicicleta=Bicicleta("Negra",2,"Urbana")
print(miBicicleta)
