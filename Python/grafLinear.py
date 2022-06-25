# importar bibliotecas
import matplotlib.pyplot as plt


# definir os intervalos dos valores de x e y
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,3,4,5,6,7,8,9,10]

# gerar o gráfico
plt.plot(x,y)

# dar nome aos eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# nome do gráfico
plt.title("Gráfico Função Linear")

# mostrar o gráfico
plt.show()