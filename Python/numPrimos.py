# Programa para verificar se um numero natural inteiro é primo


#pedir por um numero inteiro
num = int(input("Número: "))

# definir uma função que checa se um número natural inteiro é ou não é primo
def numPrimo(num):
    # se o número dado for divisível por ele mesmo ou 1
    if( num / num == 1) and (num / 1 != float):
        print("É um número primo")      # imprima "É um número primo"
    else:   # senão
        print("Não é um número primo")  #imprima "Não é um número primo"

# passar o valor num como argumento
numPrimo(num)