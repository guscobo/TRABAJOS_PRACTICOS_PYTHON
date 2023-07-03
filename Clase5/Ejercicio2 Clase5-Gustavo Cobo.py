# Ejercicio N° 2
print ("\033[H\033[J")
import numpy as npy
import matplotlib.pyplot as plt
lluvia =  [18,7,20,30,52,34,120,90,50,30,15,20]
mes = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Semptiembre","Octubre", "Noviembre","Diciembre"]
plt.bar(mes,lluvia,color='red')
plt.title("Precipitaciones año 2022")
plt.ylabel("Milimetros Caidos")
plt.xlabel("Meses")
plt.show()

