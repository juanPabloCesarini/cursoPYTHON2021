"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

"""

def pedirEdad():
    return int(input("Tu edad: "))

def mostrarEdades(edad):
    i=1
    while i<=edad:
        print("Tu edad es: ", i)
        i+=1

def main():
    edad = pedirEdad()
    mostrarEdades(edad)

main()
