"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""
def pedirClave():
    return input("Por favor ingresa una clave de 8 digitos: ")

def verificarClave(claveUsuario):
    clave = "hola1234"
    while clave != claveUsuario:
        claveUsuario= pedirClave()   
    print("Clave correcta!")

def main():
    claveUsuario = pedirClave()
    verificarClave(claveUsuario)

main()