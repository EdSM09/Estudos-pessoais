# programa que checa a data e confirm se é meu aniversário 
# ele vai servir como um teste da biblioteca datetime 
# importar a biblioteca
from datetime import date

# criar uma variável que irá armazenar a data atual
dataAtual = date.today() # definir data atual

# transformar essa data em uma string usando strftime()
dataAtualS = dataAtual.strftime("%d/%m/%y") # transformar ela em uma string no formato dd/mmm/aa

# criar uma variável com a data de aniversário
aniversario = date(2023, 3, 8)
aniversarioS = aniversario.strftime("%d/%m/%y")

# calcular a diferença em dias entre as datas 
def difDatas(dataAtual, aniversario):
    return (aniversario - dataAtual).days

# comparar a string que representa a data atual com data do meu aniversário
# imprimir se é ou não é meu aniversário
if dataAtualS == aniversarioS: # se as datas forem iguais imprima 
    print("Parabéns é seu aniversário!!!!") 
else: # se elas não forem
    print("Poxa, não é seu aniversário") # imprimima a mensagem "Poxa, não é seu aniversário"
    print("Mas faltam ", difDatas(dataAtual, aniversario), "dias") # e imprima a diferença entre as datas 
