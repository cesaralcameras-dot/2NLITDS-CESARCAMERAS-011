def sumaRecursiva(n):
    if n <=9:
        return n 
    else:
        return sumaRecursiva(n//10 )+ (n%10)


def sumaiterativa(n):
    suma =0 
    while n >0:
        suma += n%10
        n //=10
    return suma 

def main():
    cantidad= int(input("cuantos numeros va a ingresar: "))

    for i in range(1 , cantidad + 1):
        print(f"---numero {i}--")
        numero= int(input("ingrese un numero entero: "))

        print(f"suma(recursiva):{sumaRecursiva(numero)}")
        print(f"suma(iterativa):{sumaiterativa(numero)}")

if __name__=="__main__":
    main()