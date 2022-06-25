# importar a biblioteca 
import matplotlib.pyplot as plt

# valores de X
x = [1,5,6,7,8,101,12]
# valores de Y
y = [5,6,7,22,3,9,7]

# pedir para relacionar os valores de x e y e colocar no grafico
plt.plot(x, y)

# dar nomes aos eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# dar nome ao grafico
plt.title("Primeiro Gráfico")

# mostrar o gráfico
plt.show()