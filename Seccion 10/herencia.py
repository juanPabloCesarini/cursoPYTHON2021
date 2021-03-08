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
pers = Persona("Juan","Romano",27,"m")
pers.mostrarDatos()
print("--------")
class Empleado(Persona):
    def datosEmpl(self,vacaciones, sueldo):
        print("dias de vacaciones: ",vacaciones)
        print("sueldo: ", sueldo)

empleado = Empleado("Pepe", "Pompin", 23, "f")
empleado.mostrarDatos()

empleado.datosEmpl(15,50000)

