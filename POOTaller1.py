

import math;

class Persona():


    def __init__(self,nombre,edad,documento,sexo,peso,altura):
        self.__nombre=nombre
        self.__edad=edad
        self.__documento=documento
        self.__sexo=sexo
        self.__peso=peso
        self.__altura=altura

    def getnombre(self):
        return self.__nombre
    def getedad(self):
        return self.__edad
    def getdocumento(self):
        return self.__documento
    def getsexo(self):
        return self.__sexo
    def getpeso(self):
        return self.__peso
    def getaltura(self):
        return  self.__altura
    def setnombre(self,nombre):
        self.__nombre=nombre
    def setedad(self,edad):
        self.__edad=edad
    def setdocumento(self,documento):
        self.__documento=documento
    def setsexo(self,sexo):
        self.__sexo=sexo
    def setpeso(self,peso):
        self.__peso=peso
    def setaltura(self,altura):
        self.__altura=altura




    def calcularIMC(self, peso,altura):
        imc=peso/(math.pow(altura, 2))
        if imc<20:
            return -1
        if 20 <= imc <= 25:
            return 0
        if imc>25:
            return 1
    def esMayorDeEdad(self,edad):
        if edad<=17:
            return False
        return True
    def todo(self):
        print("El nombre es: "+self.__nombre+ "\nLa edad es: "+str(self.__edad))

    def generarcodigo(self):
        return self.__nombre[0:3]+str(self.__edad)+self.__documento[-3:]


miPersona=Persona("Kevin",19, "1003818315", "M", 78,183);
print(miPersona.calcularIMC(miPersona.getpeso(),miPersona.getaltura()))
print(miPersona.esMayorDeEdad(miPersona.getedad()))
miPersona.todo()
print(miPersona.generarcodigo())

