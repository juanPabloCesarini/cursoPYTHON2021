def sumar(num1,num2):
    return num1+num2

def restar(num1,num2):
    return num1-num2

def multiplicar(num1,num2):
    return num1*num2

def dividir(num1,num2):
    return num1/num2

def pedirNum():
    try:
        n1=int(input("primer numero: "))
        n2=int(input("segundo numero: "))
        return n1,n2
    except ValueError:
        print("Debes ingresar un numero")
    except Exception as e:
        print(e)

def pedirOperacion():
    op = input("Ingresar operacion (+ - * /): ")
    return op

def operar(op,num1,num2):
    if op == "+":
        print(sumar(num1,num2))
    elif op == "-":
        print(restar(num1,num2))
    elif op == "*":
        print(multiplicar(num1,num2))
    elif op == "/":
        try:
            print(dividir(num1,num2))
        except ZeroDivisionError: # intercepta el error y de esta manera se puede enviar un mensaje explicativo sin que se detenga abruptamente el programa
            print("El cero no puede ser el divisor")
        
        
    else:
        print("ERROR - No se reconoce el signo!!!")

def main():
    try:
        n1,n2=pedirNum()
        op=pedirOperacion()
        operar(op,n1,n2)
    except Exception as e:
        print(e)
    

main()