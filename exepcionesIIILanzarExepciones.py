
'''Instrcciones Raice'''
'''Creacion de exepciones porpias(Mas adelante)'''
import math
def evaluaedad(edad):
    if edad<0:
        raise TypeError("La edad no puede ser menor que 0 ")
    if edad<20:
        return "eres muy jover"
    elif edad<40:
        return "eres jover"
    elif edad<100:
        return "Cuidate"
def calcularaiz(num1):

    if  num1<0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)

print(evaluaedad(6))
ap1=(int(input("Introcuce un número : ")))
print(calcularaiz(ap1))

print ("Programa terminado")

