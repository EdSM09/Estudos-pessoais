# importar a biblioteca 
import matplotlib.pyplot as plt

# valores de X
x = [1,5,6,7,8,10,12]
# valores de Y
y = [5,6,7,2,38,9,7]

# pedir para relacionar os valores de x e y e colocar no grafico
plt.plot(x, y)

# dar nomes aos eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# 