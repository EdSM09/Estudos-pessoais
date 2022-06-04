# função que ordena uma sequência de números 
# ela toma dois argumentos a lista, e o tipo de ordem descendente DESC e ascendente ASC

def ordem(lista, tipo):
    i = 0
    if tipo.upper() == "ASC":
        for i in enumerate(lista):
            for j in range(i + 1, len(lista)):
                if lista[i] >= lista[j]:
                    t = lista[i]
                    lista[j] = lista[i]
                    lista[i] = t
                    print(lista)
    elif tipo.upper() == "DESC": 
        for i in enumerate(lista):
            for j in range(i + 1, len(lista)):
                t = lista[i]
                lista[j] = lista[i]
                lista[i] = t
                print(lista)
            


lista= [8,5,9,10,45,63]
tipo = input("Tipo de ordem: ")

print(ordem(lista, tipo))





