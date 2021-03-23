import pickle

lista = ["Juan", "Maria", "Pedro", "Luis"]
fichero = open("Seccion 13/lista_nombres.txt","wb")
pickle.dump(lista,fichero)
fichero.close()

fichero = open("Seccion 13/lista_nombres.txt","rb")
lista2 = pickle.load(fichero)
print(lista2)
fichero.close()

