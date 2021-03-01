"""
Crea una funcion con argumentos interminables, luego itera con un bucle sobre los argumentos y agregale clave y valor
"""
def con_args(*args):
    for i in args:
        print(i)
def con_kwrgs(**kwargs):
    for i in kwargs:
        print(i, "--->", kwargs[i])

def main():
    con_args("Uno",2,"pedro")
    print("************")
    con_kwrgs(pais="arg",ciudad="caba")

main()
