class Auto:
    def __init__(self):
        self.__marca = "Audi"
        self.__color = "negro"
        self.__ruedas = 4
        self.__enMarcha =False

    def __str__(self): #---> metodo para mostrar el objeto
        return "Marca: {} - Color: {} - Ruedas: {}".format(self.__marca,self.__color,self.__ruedas)

    def __arrancar(self, arrancamos):
        self.__enMarcha = arrancamos
        if self.__enMarcha:
            return "el auto esta en marcha"
        else:
            return "el auto esta detenido"
def main():
    miAuto = Auto()
    miAuto.ruedas=5 #--> al estar encapsulado el atributo no se le puede cambiar el valor por fuera de la clase
    print(miAuto.__arrancar(True)) # --> al estar encapsulado no se lo puede invocar de esta manera
    print(str(miAuto))

main()