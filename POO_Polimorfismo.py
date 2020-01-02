
class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")
class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")
class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")


#POLIMORFISMO
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


mivehiculo=Moto() #aca podemos poner Camion o Coche o Camion 
desplazamientoVehiculo(mivehiculo)