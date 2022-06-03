# Função que transforma tempo em horas em minutos
# Conseguir input do tempo em segundos
# definir uma função 
# printar o resultado final em minutos

# função para converter horas em minutos
def converter(hrs):
    return hrs * 60

# perguntar número de horas 
hrs = int(input("Horas: "))
print(converter(hrs)) # imprimir número de minutos resultantes
