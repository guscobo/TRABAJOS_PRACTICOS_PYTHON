# Ejercicio N° 7
print ("\033[H\033[J")
def cuadrado(num):
    for i in num:
        c=i%2
        if c==0:
            print("Numero par: ", i)
    return 
print("La lista de numeros a ingresara es: ")
print
numeros = (1,2,3,4,5,16,32,78,47,45)
print(list(numeros))
cuadrado(numeros)


