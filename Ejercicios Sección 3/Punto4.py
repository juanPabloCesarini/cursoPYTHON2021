"""
4: Crea una variable y asignale un valor entero. Pidele al usuario un numero por teclado, crea una variable usuario,
a la misma variable asignale una multiplicacion por 9. 
Luego multiplica en asignacion la primer variable con la segunda e imprime
en pantalla el resultado.
"""

def pedirNumero():
    return input("dame un numero entero del 1 al 9: ")

def procesar(numUsuario):
    numSecreto = 10
    numUsuario *=9
    print("El numero generado es: ", numUsuario*numSecreto)

def main():
    numUsuario = int(pedirNumero())
    procesar(numUsuario)

main()