diccionario = {
    "clave1":123,
    "clave2":True,
    "clave3":[1,2,3]
}
print(diccionario)
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())
for k,v in diccionario.items():
    print(k,v)