nombre = input("Ingresa tu nombre: ")
print("el nombre es: ", nombre.upper())

nombre = input("Ingresa tu nombre: ")
print("el nombre es: ", nombre.lower())

nombre = input("Ingresa tu nombre: ")
print("el nombre es: ", nombre.capitalize())

frase= input("Ingresa una frase: ")
letra= input("Letra a buscar: ")    

print(letra, "se encuentra: ",frase.count(letra), "veces")

print(letra, "se encuentra en la posicion: ",frase.find(letra))

print(frase.split(" "))

## HAY MAS BUSCARLAS EN LA DOCU DE PYTHON