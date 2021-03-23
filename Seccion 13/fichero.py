from io import open

fichero = open("Seccion 13/archivo.txt","w") # crea el archivo y lo prepara para la escritura
texto = "Hola Mundo\nCurso Python UDEMY"
fichero.write(texto) # se escribe el fichero con el contenido de lqa variable que se pasa por parametro
fichero.close() # se cierra el fichero
fichero = open("Seccion 13/archivo.txt","r") # prepara el fichero para la lectura
print(fichero.read()) # lee el contenido del fichero
fichero.close() # se cierra el fichero
fichero = open("Seccion 13/archivo.txt","r") # prepara el fichero para la lectura
print(fichero.readlines()) # devuelve una lista con todas las lineas separadas
fichero.close() # se cierra el fichero
fichero = open("Seccion 13/archivo.txt","a") # crea el archivo y lo prepara para agregarle lineas
fichero.write("\nNueva linea en el archivo")
fichero = open("Seccion 13/archivo.txt","r")
print(fichero.read())
fichero.close() # se cierra el fichero
