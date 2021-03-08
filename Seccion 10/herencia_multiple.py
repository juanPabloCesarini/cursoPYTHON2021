class Abuelo:
    def saludar(self):
        print("Soy la clase ABUELO o SUPERCLASE")

class Padre:
    def saludo_del_padre(self):
        print("Soy la clase PADRE o SUBCLASE")

class Tercera_generacion(Abuelo,Padre):
    def tercera(self):
        print("Soy la tercer generacion de clases")

clase = Tercera_generacion()
clase.saludar()
print("--------------")
clase.saludo_del_padre()
print("--------------")
clase.tercera()