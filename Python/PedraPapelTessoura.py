# jogo básico de pedra papel e tessoura 
# importar a biblioteca random
import random 

# opções de escolha do jogo
opções = ["pedra", "papel", "tessoura"]

# pedir a escolha do jogador em minusculo 
jogador = input("Pedra papel ou tessoura?: ").lower()
print(jogador)
# fazer o computador escolher um valor dentro da variávell opções 
computador =  random.choice(opções)
print(computador)



