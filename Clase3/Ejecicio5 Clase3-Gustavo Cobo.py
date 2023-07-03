#Ejercicio Nº 5
edad = int(input("Ingrese la edad del visitante: "))
if edad<2:
    print("Es menor de 2 años NO paga Ingreso")
elif edad<=4:
    print("Es menor de 4 años debe pagar 100 pesos para ingresar")
elif edad<=10:
    print("Es menor de 10 años debe pagar 200 pesos para ingresar")
elif edad<=18:
    print("Es menor de 19 años debe pagar 400 pesos para ingresar")   
elif edad<65:
    print("Es mayor de 18 años debe pagar 1000 pesos para ingresar")  
else:
    print("Es jubilado debe pagar 500 pesos para ingresar")

