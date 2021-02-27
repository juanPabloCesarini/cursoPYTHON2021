def invertir(texto):
    for letra in range(len(texto),0,-1):
        print(texto[letra-1], end= "")

def main():
    texto="zaid luar, 01"
    invertir(texto)

main()