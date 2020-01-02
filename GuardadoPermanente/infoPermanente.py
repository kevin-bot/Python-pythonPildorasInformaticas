import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.__nombre = nombre
        self.__genero = genero
        self.__edad = edad

        print("SE ha Creado un persona nueva cone l nombre de ", self.__nombre)
    def __str__(self):
        return "{} {} {} ".format(self.__nombre, self.__genero, self.__edad)

class ListaPersonas:
    personasLista: [] = []

    #Creamos un constructor que se encarga de crar el fichero externo

    def __init__(self):
        listaDeperonas = open("ficheroExterno", "ab+")

        listaDeperonas.seek(0)

        try:
            self.personasLista = pickle.load(listaDeperonas)
            print("Se cargaron las {} perdonas del fichero externo ".format(len(self.personasLista)))
        except:
            print("El fichero esta Vacion ")
        finally:
            listaDeperonas.close()
            del(listaDeperonas)

    def agregarPersonas(self, persona: Persona):
        self.personasLista.append(persona)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for mispersonas in self.personasLista:
            print(mispersonas)
    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas = open("ficheroExterno", "wb")
        pickle.dump(self.personasLista, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)
    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente")
        for i in self.personasLista:
            print(i)

milista: ListaPersonas = ListaPersonas()
p = Persona("Andrea","F", 20)
milista.agregarPersonas(p)

milista.mostrarInfoFicheroExterno()

