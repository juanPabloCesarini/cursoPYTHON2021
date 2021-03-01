"""
Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. 
Una dirección se considerará válida si contiene el símbolo "@".
"""
def pedirMail():
    return input("Ingresar un mail: ")

def validarMail(mail):
    if "@" in mail:
        print("mail correcto")
    else:
        print("mail invalido")

def main():
    mail=pedirMail()
    validarMail(mail)

main()