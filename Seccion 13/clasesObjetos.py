import pickle
class Gelatina: # Nombre de la clase siempre en mayusculas
    def __init__(self, sabor,color,tamanio): #--> constructor
        self.sabor = sabor #--> atributo
        self.color = color #--> atributo
        self.tamanio = tamanio #--> atributo
    
    # metodos

    def imprimir(self):
        print("La gelatina de {} tiene es de color {} y su tamaño es {}".format(self.sabor,self.color,self.tamanio))



def main():
    gel1 = Gelatina("frutilla", "rojo", "grande") #---> Atributos pasados por parámetros
    gel1.imprimir()
    gel2 = Gelatina("anana", "amarillo", "grande")
    lista_gelatina = [gel1,gel2]
    fichero3 = open("Gelatina","wb")
    pickle.dump(lista_gelatina, fichero3)
    fichero3.close()
    del(fichero3)
    fichero4 = open("Gelatina", "rb")
    laGelatina = pickle.load(fichero4)
    fichero4.close()
    for i in laGelatina:
        print(i.sabor + " -- " + i.color + " -- " + i.tamanio)

main()