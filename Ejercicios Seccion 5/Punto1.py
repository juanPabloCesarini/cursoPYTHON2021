"""
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

"""
def armarLista():
    materias=["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
    return materias

def mostrarMaterias(materias):
    for materia in materias:
        print(materia, end=" ")

def main():
    materias=armarLista()
    mostrarMaterias(materias)

main()