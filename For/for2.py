#Leer un numero introducido por el usuario
#Mostrar la letra a por cada numero del 1 al numero
#Ingresado por el usuario ejemplo, Numero 3: 
#a
#aa
#aaa

def mostrarLetra(numero):
    for i in range(1,numero + 1):
        print(f"a"*i)

def main():
    num = int(input("Ingrese un numero: "))
    mostrarLetra(num)

main()