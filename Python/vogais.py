# Programa que conta o número de vogais dento de um texto

def vogais(txt):
    for i in range(len(txt)):
        if txt[i] == 'a' or 'o' or 'i' or 'u':
             counter += 1
             return counter

# pedir imput de texto do usuário 
txt = input("Texto: ")
counter = vogais(txt)

# print(txt) # confirmar a entrada do input


print("O numero de vogais é {0} ".format(counter))

