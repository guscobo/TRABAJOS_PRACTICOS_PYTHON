# Ejercicio N° 4
print ("\033[H\033[J")
def totfactura(tot,iva):
    factura = tot+tot*iva/100
    print("El total de la factura es ",factura)
    return factura
tot = int(input("Ingrese el total de la factura: "))
totfactura(tot,21)

