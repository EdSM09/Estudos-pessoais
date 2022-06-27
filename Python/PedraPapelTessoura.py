# jogo básico de pedra papel e tessoura 
# importar a biblioteca random
import random 

# opções de escolha do jogo
opções = ["pedra", "papel", "tessoura"]

# fazer um loop while para repetir o jogo
while True:
    # pedir a escolha do jogador em minusculo 
    # garantir que o input é uma das opções do jogo
    jogador = None
    while jogador not in opções:
        jogador = input("Pedra papel ou tessoura?: ").lower()
        print(jogador)

    # fazer o computador escolher um valor dentro da variávell opções 
    computador =  random.choice(opções)
    print(computador)


    # criar os if statements de acordo com as regras do jogo 
    # empate
    if jogador == computador:
        print("Empate! ")
    # pedra
    elif jogador == "pedra":
        if computador == "tessoura":
            print("Você ganhou!!!!!")
        if computador == "papel":
            print("Você perdeu!")
    # papel 
    elif jogador == "papel":
        if computador == "pedra":
            print("Você ganhou!!!!!")
        if computador == "tessoura":
            print("Você perdeu!")

    # tessoura
    elif jogador == "tessoura":
        if computador == "papel":
            print("Você ganhou!!!!!")
        if computador == "pedra":        
            print("Você perdeu!")
    jogarNovamente = input("Você que jogar de novo (sim/não)?: ").lower()
    
    if jogarNovamente != "sim":
        break
print("Tchaul!")

        