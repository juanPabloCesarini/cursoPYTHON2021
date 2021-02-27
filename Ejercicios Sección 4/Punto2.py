"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

"""
def pedirPalabra():
    return input("Ingresar palabra: ")

def mostrar(pal):
    i = 1
    while i <= 10:
        print(i , "->", pal)
        i+=1

def main():
    palabra = pedirPalabra()
    mostrar(palabra)

main()