

class Vehiculo():
    def __init__(self, color, ruedas ):
         self.__color=color
         self.__ruedas=ruedas
    def __str__(self):
        pass

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color,ruedas)
        self.__velocidad = velocidad
        self.__cilindrada = cilindrada

    def getcolor(self):
        return self.__velocidad



class Camioneta(Coche):
   def __init__(self, carga):
       self.__carga = carga


class Bicicleta(Vehiculo):
    def __init__(self, tipo):
        self.__tipo=tipo

class Motocicleta(Bicicleta):
    def __init__(self, velocidad, cilindrada):
        self.__velocidd=velocidad
        self.__cilindrada=cilindrada


michoce= Coche("rojo",4,100, 5300);
listavehiculos = [michoce]

print(listavehiculos[0].getcolor())



