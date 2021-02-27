"""3: Con operadores logicos, determina si una cadena de texto ingresada por el usuario
tiene una longitud mayor o igual a 3 y a su vez es menor a 10. (tru o false)"""

def pedirTexto():
    return input("Ingresar texto: ")

def evaluar(texto):
    longitudTexto = len(texto)
    if longitudTexto >= 3 and longitudTexto < 10:
        print(True)
    else:
        print(False)

def main():
    texto = pedirTexto()
    evaluar(texto)

main()
