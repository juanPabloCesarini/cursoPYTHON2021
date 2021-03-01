"""
Crea una funcion que nos devuelva numeros pares.
"""
def nrosPares(limite):
    for i in range(1,limite,1):
        if i%2==0:
            print(i)
    if limite%2==0:
        print(limite)
def pedirLimite():
    return int(input("Ingresa un nro tope para buscar numeros pares: "))

def main():
    lim = pedirLimite()
    nrosPares(lim)

main()
