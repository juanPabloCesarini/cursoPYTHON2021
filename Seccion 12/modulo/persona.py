class Persona:
    def __init__(self, nombre, apellido, edad, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo

    def mostrarDatos(self):
        print("Nombre: ",self.nombre)
        print("Apellido: ",self.apellido)
        print("Edad: ",self.edad)
        print("Sexo: ",self.sexo)
