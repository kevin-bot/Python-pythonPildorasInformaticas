
lista=[1,2,3,4,5,6]


def llenarlista(valor):
    return [valor]

def mostrarlista(lista):
        print(lista)

def acturalizar(milista, valorbuscar,valor):
    if valorbuscar in milista:
        milista.insert(milista.index(valorbuscar),valor)

def eliminar(milista, valoreliminar):
    if valoreliminar in milista:
        milista.remove(valoreliminar)

def agregaraLista(milista,valoragregar):
    if valoragregar not in milista:
        milista.append(valoragregar)


salir=True
while salir:
        opcion=input("Seleccione una opcion: \n"
                     "1) Agregar a la lista\n"
                     "2) Eliminar de la lista\n"
                     "3) Actualizar de la lista\n"
                     "4) Mostar lista\n"
                     "0) Salir\n")
        valor=(int(input("Introdusca el valor: ")))
        if opcion=="1":
            agregaraLista(lista,valor)
        if opcion=="2":
            eliminar(lista,5)
        if opcion=="3":
            acturalizar(lista,1,99)
        if opcion=="4":
            mostrarlista(lista)
        if opcion=="0":
            break

