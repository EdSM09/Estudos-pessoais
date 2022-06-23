# Programa para verificar se um numero inteiro é primo


#pedir por um numero inteiro
num = int(input("Número: "))

def numPrimo(num):
    if( num / num == 1) and (num / 1 != float):
        print("É um número primo")

numPrimo(num)