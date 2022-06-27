# programa que checa a data e confirm se é meu aniversário 
# ele vai servir como um teste da biblioteca datetime 
# importar a biblioteca
from datetime import date

# criar uma variável que irá armazenar a data atual
dataAtual = date.today() # definir data atual

# transformar essa data em uma string usando strftime()
dataAtualS = dataAtual.strftime("%d/%m/%y") # transformar ela em uma string no formato dd/mmm/aa
print(dataAtualS) # imprimir data para confirmar 

# comparar a string que representa a data atual com data do meu aniversário
# criar uma variável com a data de aniversário
aniversario = date(2023, 3, 8)
aniversarioS = aniversario.strftime("%d/%m/%y")
print(aniversarioS) # imprimir para confirmar 
# imprimir se é ou não é meu aniversário
# calcular a diferença em dias entre as datas 