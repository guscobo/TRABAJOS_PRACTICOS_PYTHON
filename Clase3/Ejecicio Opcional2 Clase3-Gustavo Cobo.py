#Ejercicio Opcional 2
nume = int(input("Ingrese un numero: "))
for i in range(1,nume+1,2):
    for j in range(1,i+1,2):
        print(i+1-j,end=" ")
    print("")

