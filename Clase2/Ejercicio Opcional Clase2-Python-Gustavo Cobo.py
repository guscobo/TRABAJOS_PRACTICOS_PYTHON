#Ejercicio OPCIONAL

capi=int(input("Ingrese la Herencia o el Capital: "))
pfijoanual = (((((capi*1.5)*1.5)*1.5)*1.5)*1.5)
mes1 = ((((((((((((capi*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)
mes2 = ((((((((((((mes1*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)
mes3 = ((((((((((((mes2*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)
mes4 = ((((((((((((mes3*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)
bonos = ((((((((((((mes4*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)*1.035)
 
print ("La inversion por Plazo Fijo a los 5 años es de: ",round(pfijoanual,2))
print ("La inversion por bonos a los 5 años es de: ",round(bonos,2))
mayor = max(pfijoanual,bonos)
print("La mejor inversion es", round(mayor,2))

