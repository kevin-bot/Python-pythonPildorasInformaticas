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



fichero_apertura = open("laspersonas", "rb")

misPersonas = pickle.load(fichero_apertura) #cargar la informacion

fichero_apertura.close()

for i in misPersonas:
    print(i.descripcion())