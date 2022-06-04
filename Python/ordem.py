lista = [1,5,3,8,9,40,50]
tipo = input("Tipo: ")
print(lista)

if tipo.upper()== "ASC":
    lista.sort()
    print(lista)
elif tipo.upper()== "DESC":
    lista.sort(reverse = True)  
    print(lista)
elif tipo.upper()== "NONE":
    print(lista)
