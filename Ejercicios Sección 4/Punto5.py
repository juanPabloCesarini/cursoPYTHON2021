"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario 
tiene que tributar o no.
"""
def pedirDatos():
    edad =int(input("Ingresar edad: "))
    ingreso = float(input("Ingresar sueldo: "))
    return edad , ingreso

def evaluar(edad, ingreso):
    if edad>16 and ingreso >=1000:
        print("Hay que tibutar")
    else:
        print("No se tributa")

def main():
    edad , ingreso = pedirDatos()
    evaluar(edad,ingreso)

main()