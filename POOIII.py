
class Coche():

    def __init__(self):
        self.__largoChachsis=250
        self.__anchochasis=120
        self.__ruedas=4
        self.__enmarcha=False

    def getlargo(self):
        return self.largoChachsis

    def setlargo(self, largo):
        self.largoChachsis=largo



micoche=Coche()

print(micoche.getlargo())
micoche.setlargo(500)
print(micoche.getlargo())