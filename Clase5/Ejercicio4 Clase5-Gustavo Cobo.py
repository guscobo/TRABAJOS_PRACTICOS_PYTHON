#Ejercicio OPCIONAL    
print ("\033[H\033[J")
import numpy as npy
import matplotlib.pyplot as plt
tempTrelew =  [4,4,4,4,3,3,3,3,2,2,4,6,8,9,11,11,11,11,9,11,8,6,4,4]
tempObera =  [18,19,18,18,18,18,18,18,19,21,23,24,25,26,26,27,24,22,21,20,19,19,19,18]
hora = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
plt.plot(hora,tempObera, 'r-^')
plt.plot(hora,tempTrelew, 'b-^')
plt.title("Dia 27/06/2023", color ='g')
plt.suptitle("Temperaturas de Trelew Chubut y Oberá Misiones", color ='g')
plt.annotate('Trelew', xy = (0,5), color = 'b')
plt.annotate('Obera', xy = (0,20), color = 'r')
plt.ylabel("Temperaturas en Grados")
plt.xlabel("Horario")
plt.show()

