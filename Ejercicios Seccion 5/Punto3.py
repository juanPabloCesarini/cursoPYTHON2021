"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""
def pedirDatos():
    nombre = input("Ingresá tu nombre: ")
    edad = input("Tu edad: ")
    dire = input("Donde vivis? ")
    tel = input("Teléfono: ")
    return nombre,edad,dire,tel

def guardarDatos(nombre,edad,dire,tel):
    agenda = {nombre:{"edad":edad,"dire":dire,"tel":tel}}
    return agenda

def mostrarAgenda(agenda):
    for dato in agenda:
        datosAgenda = agenda[dato]
        print("Nombre:", dato, "tiene", datosAgenda["edad"], "años, vive en", datosAgenda["dire"], " y su número de teléfono es", datosAgenda["tel"])

def main():
    n,e,d,t = pedirDatos()
    agenda=guardarDatos(n,e,d,t)
    mostrarAgenda(agenda)

main()
