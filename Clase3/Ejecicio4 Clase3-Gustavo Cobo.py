#Ejercicio Nº 4
harina = int(input("Ingrese los kilos de harina: "))
if harina==5:
    azucar = int(input("Ingrese los kilos de azucar: "))
    if azucar==1:
        manteca = int(input("Ingrese los kilos de manteca: "))
        if manteca==2:
            print("Se puede preparar la receta del PAN")
        else:
            print("No se puede preparar la receta del PAN")
            print("Se necesitan 2 kilos de manteca")
    else:
        print("No se puede preparar la receta del PAN")
        print("Se necesitan 1 kilo de azucar")    
else:
    print("No se puede preparar la receta del PAN")
    print("Se necesitan 5 kilos de harina") 

