# jogo básico de pedra papel e tesoura 
# importar a biblioteca random
import random 

# opções de escolha do jogo
opções = ["pedra", "papel", "tesoura", "lagarto", "spock"]

#variavel que armazena os pontos
pontos = 0
# fazer um loop while para repetir o jogo
while True:
    # pedir a escolha do jogador em minusculo 
    # garantir que o input é uma das opções do jogo
    jogador = None
    while jogador not in opções:
        jogador = input("Pedra, papel, tesoura, lagarto ou spock?: ").lower()

    # fazer o computador escolher um valor dentro da variávell opções 
    computador =  random.choice(opções)


    # criar os if statements de acordo com as regras do jogo 
    # empate
    if jogador == computador:
        print("Jogador: ",jogador)
        print("Computador: ",computador)
        print("Empate! ")
    # pedra
    elif jogador == "pedra":
        if computador == "tesoura":
            print("Jogador: ",jogador)
            print("Computador: ",computador)
            print("Você ganhou!!!!!")
            pontos = pontos + 1
            
        if computador == "papel":
            print("Jogador: ",jogador)
            print("Computador: ",computador)
            print("Você perdeu!")
            
        if computador == "lagarto":
            print("Jogador: ",jogador)
            print("Computador: ",computador)  
            print("Você ganhou!!!!!")
   
        if computador ==  "spock":
            print("Jogador: ",jogador)
            print("Computador: ",computador)
            print("Você perdeu!")
 
    # papel 
    elif jogador == "papel":
        if computador == "pedra":
            print("Jogador: ",jogador)
            print("Computador: ",computador)
            print("Você ganhou!!!!!")
            
        if computador == "tesoura":
            print("Jogador: ",jogador)
            print("Computador: ",computador)
            print("Você perdeu!")
            
        if computador == "lagarto":
            print("Jogador: ",jogador)
            print("Computador: ",computador)
            print("Você perdeu!")
            
        if computador == "spock":
            print("Jogador: ",jogador)
            print("Computador: ",computador)
            print("Você ganhou!!!!!")
    # tesoura
    elif jogador == "tesoura":
        if computador == "papel":
            print("Jogador: ",jogador)
            print("Computador: ",computador)
            print("Você ganhou!!!!!")
            
        if computador == "pedra":   
            print("Jogador: ",jogador)
            print("Computador: ",computador)     
            print("Você perdeu!")
            
        if computador == "lagarto":
            print("Jogador: ",jogador)
            print("Computador: ",computador)     
            print("Você ganhou!!!!!")
            
        if computador == "spock":
            print("Jogador: ",jogador)
            print("Computador: ",computador)     
            print("Você perdeu!")
          
    # lagarto
    elif jogador == "lagarto":
        if computador == "pedra":
            print("Jogador: ",jogador)
            print("Computador: ",computador)     
            print("Você perdeu!")
            
        if computador == "papel":
            print("Jogador: ",jogador)
            print("Computador: ",computador)
            print("Você ganhou!!!!!")
            
        if computador == "tesoura":
            print("Jogador: ",jogador)
            print("Computador: ",computador)     
            print("Você perdeu!")
            
        if computador == "spock":
            print("Jogador: ",jogador)
            print("Computador: ",computador)
            print("Você ganhou!!!!!")
    # spock
    elif jogador == "spock":
        if computador == "pedra":
            print("Jogador: ",jogador)
            print("Computador: ",computador)
            print("Você ganhou!!!!!")
    
        if computador == "papel":
            print("Jogador: ",jogador)
            print("Computador: ",computador)     
            print("Você perdeu!")
   
        if computador == "tesoura":
            print("Jogador: ",jogador)
            print("Computador: ",computador)
            print("Você ganhou!!!!!")

            
        if computador == "lagarto":
            print("Jogador: ",jogador)
            print("Computador: ",computador)     
            print("Você perdeu!")

            
    jogarNovamente = input("Você que jogar de novo (sim/não)?: ").lower()
    
    if jogarNovamente != "sim":
        break
print("Tchaul!")