#El usuario digita un numero y el programa imprime la tabla de multiplicar hasta el 10
def tablaMultiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def main():
    numero = int(input("Ingrese un numero para mostrar su tabla de multiplicar: "))
    tablaMultiplicar(numero)

main()
