class Gelatina: # Nombre de la clase siempre en mayusculas
    def __init__(self, sabor,color,tamanio): #--> constructor
        self.sabor = sabor #--> atributo
        self.color = color #--> atributo
        self.tamanio = tamanio #--> atributo
    
    # metodos

    def imprimir(self):
        print("La gelatina de {} tiene es de color {} y su tamaño es {}".format(self.sabor,self.color,self.tamanio))

class Auto:
    def __init__(self):
        self.marca = "Audi"
        self.color = "negro"
        self.ruedas = 4
        self.enMarcha = False

    def arrancar(self, arrancamos):
        self.enMarcha = arrancamos
        if self.enMarcha:
            return "el auto esta en marcha"
        else:
            return "el auto esta detenido"

    def __str__(self):
        return "Auto marca {}, de color {} y tiene {} ruedas".format(self.marca,self.color,self.ruedas)

def main():
    gel1 = Gelatina("frutilla", "rojo", "grande") #---> Atributos pasados por parámetros
    gel1.imprimir()
    print("-----------------------")
    miAuto = Auto() # ---> En este caso los atributos están definidos en el constructor
    print(miAuto.arrancar(True))
    print(str(miAuto))


main()