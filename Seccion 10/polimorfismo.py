class Persona:
    def __init__(self):
        self.cedula = 1234

    def mensaje(self):
        print("Mensaje clase persona")

class Obrero(Persona):
    def __init__(self):
        self.especialidad = 1
    
    def mensaje(self):
        print("mensaje clase obrero ")
        

obrero_planta = Persona()
obrero_planta.mensaje()

####
class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print("guau")

class Gato(Animal):
    def hablar(self):
        print("miau")

unPerro = Perro()
unGato = Gato()

unPerro.hablar()
unGato.hablar()