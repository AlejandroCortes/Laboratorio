import numpy as np
import matplotlib.pyplot as plt
import sys

resultados = np.loadtxt("Solucion.dat")


x = resultados[:,0]
y = resultados[:,1]



plt.plot(x,y)
plt.title("Solucion de la Eq diferencial")
plt.xlabel("valores de X")
plt.ylabel("valores de y")
plt.savefig("graficafinal.jpg")
