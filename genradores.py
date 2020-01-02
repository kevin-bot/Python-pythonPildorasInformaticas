



#generadores: son mas eficientes de las funciones
# mostrar uno en uno
#muy útiles con listra de valores infinitos
#Bajo determinados escenarios, sera muy util que un generador devuelva los valores de uno en uno


#crear un metodo para que haga una lista de numeros pares
def generarpares(limite):
    numero=1
    milista=[]
    while numero<limite:
            milista.append(numero*2)
            numero+=1
    return milista
print(generarpares(10))

#los mismo con un generador

def generador(limite):
    numero = 1
    while numero < limite:
        yield numero*2
        numero+=1
devulvepares=generador(10)

print(next(devulvepares))


#entrar a elementos dentro de otros elementos
# una especie de matriz

#cuando colocamos el * va arecivir unnumero determinado de argumentos, y ademas los almacene el tupla

def generadorciudades(*ciudades):
    for i in ciudades:
        #for j in i:
            yield from i

ciudadesdevultas = generadorciudades("Madrid","sevilla", "caicedonia")
print("Los elementos que estann dentro de los elementos principales son ")
print(next(ciudadesdevultas))
print(next(ciudadesdevultas))