"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y 
la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

"""
def armarLista():
    materias=["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
    return materias

def mostrarMaterias(materias):
    for materia in materias:
        print("Yo estudio", materia)

def main():
    materias=armarLista()
    mostrarMaterias(materias)

main()