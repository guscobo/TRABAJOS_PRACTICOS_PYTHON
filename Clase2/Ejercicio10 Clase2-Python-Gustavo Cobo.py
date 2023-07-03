#Ejercicio Nº10

capi=int(input("Ingrese la Herencia o el Capital: "))
pfijo = (((((capi*1.5)*1.5)*1.5)*1.5)*1.5)
bonos = ((((((((((capi*1.25)*1.25)*1.25)*1.25)*1.25)*1.25)*1.25)*1.25)*1.25)*1.25)
print ("La inversion por Plazo Fijo a los 5 años es de: ",round(pfijo,2))
print ("La inversion por bonos a los 5 años es de: ",round(bonos,2))
mayor = max(pfijo,bonos)
print("La mejor inversion es", round(mayor,2))

