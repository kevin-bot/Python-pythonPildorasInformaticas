

#se importa la libreria io con su metodo open
from io import open

# se crea un nombre del archivo que va a ser igual al metodo open elcual no pide dos parametros
# uno es el nombre del archivo que vamos abrir, el otro el modo en el que lo vamos a leer lectura, escritura, ..


# si se ejecuta tal como esta aca el codigo, veremos que nos crea un archivo con el nombre archivo.txt vacio
archivo_texto = open("archivo.txt", "w")  #face de creacion y apertura

frase = "Estupendo día para estudiar Python \n el miércoles"

#utilizando la variable archivo_texto y el metod write podemos esrcribir el el arvhio.txt

archivo_texto.write(frase)  #face de manipulacion

archivo_texto.close() #face de cierre


#para leer el contenido del archivo utilizamos el metodo read

archivo_texto = open("archivo.txt", "r") #leemos el archivo con eviandole como segundo parametro una r

texto = archivo_texto.read() #leemos el contenido del archivo y lo almacenamos en la variable texto

archivo_texto.close()

# no importa que ta se haya cerrado el archivo el contenido sigue en la variable texto

print(texto)

#reordad que podemos añadir mas informacion
# se puede leer la informacion y almacenar dentro de una lista