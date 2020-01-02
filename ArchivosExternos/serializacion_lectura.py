import pickle

fichero = open("lista_nombres","rb") #leemos el archivo binario

lista = pickle.load(fichero)

print(lista)