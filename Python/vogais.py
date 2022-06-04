# Programa que conta o número de vogais dento de um texto


# função que toma como argumento a variável string e retorna um valor int que representa a quantidade de vogais no texto
def contarVogais(string):
    
    string = string.lower() # formatar o texpo para caracteres minusculos
    vogais = 'a,e,i,o,u' #definir as vogais
    resultado = 0 # um contador que vai armazenar o resultado
    for i in vogais: # para todos os valores de i em vogais
        resultado += string.count(i) # some o resultado com a quantidade de caracteres i equivalentes em string e vogais
    return resultado # devolver o número de vogais 
    
# pegar o texto do usuário   
string = input("texto: ")     
# imprimir a quantidade de vogais do texto obtido        
print(contarVogais(string))

