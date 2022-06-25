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
plt.title('Colored Circle')
plt.show()

# metodo 2
