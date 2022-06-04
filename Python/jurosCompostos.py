# Programa que calcula os juros compostos de um capital 

# Definir função que calcula o montante funal depois de n meses 
def jurosCompostos(cap, taxa, n):
    #retornar o vaalor do montante
    montante= cap * (1 + taxa) ** (n)
    return montante
    
# Pedir paraa que o usuário de a quantidade inicial, taxa de juros e tempo em meses
cap = int(input("Capital aplicado: ")) 
taxa = float(input("Taja de juros compostos: "))
n = int(input("Tempo: "))

# Imprimir montante
print("O montante final é {0}".format(jurosCompostos(cap, taxa, n)) + " reais")

# Imprimir o valor dos juros 
print("O valor dos juros é {0}".format(jurosCompostos(cap, taxa, n) - cap) + " reais")