# Ejercicio N° 3
print ("\033[H\033[J")
def factorial(num):
    a = 1
    for i in range(1,num+1):
        a = a * i
    print("El factorial de",num,"es", a)
    return a
num = int(input("Ingrese un numero: "))
factorial(num)

