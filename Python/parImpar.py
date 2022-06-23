# programa que aceita um array de numeros inteiros e determina se são par ou impar


# criar uma lista
num = list(range(0, 1000))
# print(num)

# definir função que para o compriento da lista cheque a condição par ou impar
def imparPar(num):
    for i in range(len(num)):
        if num[i] % 2 == 0:
            print("Par!")
        else:
            print("Impar!")
imparPar(num)