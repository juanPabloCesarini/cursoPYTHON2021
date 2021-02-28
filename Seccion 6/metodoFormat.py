# EJEMPLOS PARA USAR EL METODO FORMAT

nombre = "Juan"
edad = 46
pais ="Argentina"

print("Me llamo {} y tengo {}".format(nombre,edad))

#usando indices
print("Me llamo {0} y tengo {1}, vivo en {2}".format(nombre,edad, pais))

#usando claves

n = "Juan"
e = 46
p ="Argentina"

print("Me llamo {nombre} y tengo {edad}, vivo en {pais}".format(nombre=n,edad=e, pais=p))