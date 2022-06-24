# programa que gera diferentes modelos de piramide dependendo do input do usuário

# pedir a altura da pirâmide
altura = int(input("Altura da Pirâmide: "))
# pedir o tipo da pirâmide
tipo = input("Tipo: ").upper()

# definir as funções de cada piramide

# pirâmide completa ponta ara cima
def piramideCima(altura):
    for i in range(altura):
        for j in range(altura- i - 1):
            print(" ", end=" ")
        for k in range(2 * i + 1):
            print("#", end=" ")
        print( )
            
# pirâmide completa ponta para baixo
def piramideBaixo(altura):
    for i in range(altura, 0, -1): 
        for j in range(altura -  i):
            print(" ", end=" ")
        for j in range(2 * i - 1):
            print("#", end=" ")
        print( )
        
# meia pirâmide direita
def piramideEsquerda(altura):
    for i in range(1, altura + 1):
        for j in range(1, i + 1):
            print("#", end=" ")
        print( )
        
# meia pirâmide esqueda
def piramideDireita(altura):
    for i in range(altura):
        for j in range(1, altura - 1):
            print(" ", end=" ")
        for k in range(0, i + 1):
            print("#", end=" ")
        print( )
        
# if elif statements para checar os tipos e imprimir as pirâmides
if tipo == "CIMA":
    piramideCima(altura)
    
elif tipo == "BAIXO":
    piramideBaixo(altura)
    
elif tipo == "DIREITA":
    piramideDireita(altura)
    
elif tipo == "ESQUERDA":
    piramideEsquerda(altura)

