# Ejercicio N° 1
print ("\033[H\033[J")
import numpy as npy
import matplotlib.pyplot as plt
temperatura =  [10,9,9,9,9,8,7,10,10,11,13,14,14,15,16,15,14,13,12,11,10,9,9,8]
hora = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
plt.plot(hora,temperatura)
plt.title("Temperaturas del dia 26/06/2023")
plt.ylabel("Temperaturas en Grados")
plt.xlabel("Horario")
plt.show()

