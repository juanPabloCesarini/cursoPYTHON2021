"""
Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.
"""
def pedirNombre():
    nombre = input("Escibi tu nombre: ")
    return nombre

def saludar(nombre):
    print("Hola {}!".format(nombre))

def main():
    n=pedirNombre()
    saludar(n)

main()