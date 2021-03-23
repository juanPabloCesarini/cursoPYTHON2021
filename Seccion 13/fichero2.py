from io import open
fichero = open("Seccion 13/archivo2.txt","w")
texto="capitulo de cursores"
fichero.write(texto)
fichero.close()
fichero = open("Seccion 13/archivo2.txt","r")
fichero.seek(9) # mueve el cursor para indicar a partir de donde mostrar los datos
print(fichero.read())
fichero.close()
fichero = open("Seccion 13/archivo2.txt","r")
print(fichero.read(4)) # muestra desde el inicio hasta el final pasado por parametro
fichero.close()
fichero = open("Seccion 13/archivo2.txt","r")
fichero.seek(len(fichero.read())/2)
print(fichero.read())
fichero.close()