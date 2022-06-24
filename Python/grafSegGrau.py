# importar biblioteca
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-100,1000,1)

y = x ** 2 

plt.plot(x, y)

# dar nomes aos eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# dar nome ao grafico
plt.title("Gráfico")

plt.show()
