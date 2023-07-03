# Ejercicio N° 5
print ("\033[H\033[J")
def promedio(*num):
    tot = 0
    p = 0
    for i in num:
        p=p+1
        tot=tot+i
    print(" El promedio de la lista de numeros es:",tot/p)
    return 
promedio(1,2,3,4,5,16,32,78)

