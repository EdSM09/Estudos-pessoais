# programa que checa a data e confirm se é meu aniversário 
# ele vai servir como um teste da biblioteca datetime 
# importar a biblioteca
from datetime import date

# criar uma variável que irá armazenar a data atual
dataAtual = date.today()
dataAtualS = dataAtual.strftime("%d%m%y")
print(dataAtualS)
# transformar essa data em uma string usando strftime()

# comparar a string que representa a data atual com data do meu aniversário

# imprimir se é ou não é meu aniversário
# calcular a diferença em dias entre as datas 