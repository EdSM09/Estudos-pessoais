# como ordenar listas
# definir a lista como um array de valores int
lista = [1,5,3,8,9,40,50]
# pedir o tipo de ordem, crescente ou decrescente 
tipo = input("Tipo: ")
# imprimir lista original
print(lista)

# Se o tipo for ASC organize a lista de forma crescente
if tipo.upper()== "ASC":
    lista.sort()
    print(lista)
    
# Se o tipo for DESC organize a lista de forma decrescente
elif tipo.upper()== "DESC":
    lista.sort(reverse = True)  
    print(lista)
    
# Se o tipo for NONE imprima lista como esta 
elif tipo.upper()== "NONE":
    print(lista)
