# programa que imprimi um grafico de um circulo
# inplementar a biblioteca
import matplotlib.pyplot as plt 
import numpy as np



# tentar alguns metôdos da internet

# metodo 1
figure, axes = plt.subplots()
cc = plt.Circle((0.5 , 0.5), 0.4)

axes.set_aspect(1)
axes.add_artist(cc)
plt.title("Circulo Colorido")
plt.show()

# metodo 2
angulo  = np.linspace(0 , 2 * np.pi , 150)

raio = 0.4

x =  raio * np.cos(angulo)
y = raio * np.sin(angulo)

figure , axes = plt.subplots(1)

axes.plot(x, y, edgecolors= 'red')
axes.set_aspect(1)

plt.title("Circuferência")