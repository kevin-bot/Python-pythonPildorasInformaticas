
import pickle

class Persona():
    def __init__(self, nombre,edad,lugarResidencia):
        self.__nombre=nombre;
        self.__edad=edad;
        self.__lugarResidencia=lugarResidencia
    def descripcion(self):
        print ("Nombre: ", self.__nombre, " Edad : ", self.__edad, "Residencia: ", self.__lugarResidencia)


class Empleado(Persona):
    def __init__(self, salario,antiguadad,nombre,edad,recidencia):
        super().__init__(nombre,edad,recidencia)
        self.__salario=salario
        self.__antiguadad=antiguadad
    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.__salario, " Antiguadad: ", self.__antiguadad)


mipersona1 = Empleado(500000,15,"kevin",19,"Colombia")
mipersona2 = Empleado(500000,15,"santiago",19,"Colombia")
mipersona3 = Empleado(500000,15,"Daniela",19,"Colombia")

#para no serializar uno en uno los obejetods, se crea una lista de onjetos

personasList = [ mipersona1, mipersona2, mipersona3]

fichero = open("laspersonas", "wb")

pickle.dump(personasList,fichero)

fichero.close()

del(fichero)

