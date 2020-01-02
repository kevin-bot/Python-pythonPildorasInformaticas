
import pickle

lista_nombres  = ["Pedro", "Ana", "Maria", "Daniela"]

fichero_binario = open("lista_nombres","wb") #creamos el archivo con permisos de escritura binaria (wb)

#hacer el volvado

pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()

del(fichero_binario)