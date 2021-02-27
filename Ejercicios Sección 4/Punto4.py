"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""
def pedirX():
    return input("ingresar algo o salir para terminar: ")

def imprimirEco(X):
    while X != "salir":
        print(X)
        X=pedirX()
    print("fin")

def main():
    X = pedirX()
    imprimirEco(X)

main()