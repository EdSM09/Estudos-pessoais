# importar biblioteca
import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(-100,1000,1)
x2 = np.arange(-100,1000,1)

y1 = x1 ** 2 
y2 = x2 ** 6

plt.plot(x, y)

# dar nomes aos eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# dar nome ao grafico
plt.title("Gráfico")

plt.show()
