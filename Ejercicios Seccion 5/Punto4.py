"""
Mete los valores del 1 al 100 en una lista.
"""
def guardarEnLista():
    lista =[]
    for i in range(1,101,1):
        lista.append(i)
    print(lista)

def main():
    guardarEnLista()

main()