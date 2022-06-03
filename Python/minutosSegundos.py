# Função que transforma tempo em minutos em segundos
# Conseguir input do tempo em segundos
# definir uma função 
# printar o resultado final em segundos 


# função toma uma int min como argumento e retorna a multiplicação desse valor por 60
def converter( min):
    return min * 60

# perguntar o número de minutos para converter
min = int(input("Minutos: "))
print(converter(min))

