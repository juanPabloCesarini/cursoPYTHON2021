def pedirNumeros():
    num1 = int(input("Ingresar un número entero: "))
    num2 = int(input("Ingresar otro número entero: "))
    return num1,num2

def evaluar(num1,num2):
    if num1 == num2:
        print(num1 , "y" , num2 , "son iguales")
    else:
        print(num1 , "y" , num2 , "son distintos","\n")
        if num1 > num2:
            print(num1 , "es mayor a" , num2 ,"\n")
        else:
            print(num1 , "es menor a" , num2 ,"\n")

def main():
    x,y = pedirNumeros()
    evaluar(x,y)

main()