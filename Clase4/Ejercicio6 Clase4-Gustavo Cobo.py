# Ejercicio N° 6
print ("\033[H\033[J")
def cuadrado(*num):
    for i in num:
        c=i*i
        print("EL cuadrado del numero: ", i, "es",c)
    return 
cuadrado(1,2,3,4,5,16,32,78)

