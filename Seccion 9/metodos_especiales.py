class Auto:
    def __init__(self, marca, km , modelo): #---> metodo constructor
        self.marca = marca
        self.km = km
        self.modelo = modelo
        print("Se creó el objeto Auto", self.marca)
    
    def __del__(self): #---> metodo destructor
        print("Se destruyó objeto auto", self.marca)

    def __str__(self): #---> metodo para mostrar el objeto
        return "Marca: {} - KM: {} - Modelo: {}".format(self.marca,self.km,self.modelo)
def main():
    miAuto = Auto("VW Gol", 150000, 1998)
    print(str(miAuto))
    del(miAuto)

main()
