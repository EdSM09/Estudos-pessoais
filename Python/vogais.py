# Programa que conta o número de vogais dento de um texto

def contarVogais(string):
    string = string.lower()
    vogais = 'a,e,i,o,u'
    resultado = 0
    for i in vogais:
        resultado += string.count(i)
    return resultado
    
    
string = input("texto: ")             
print(contarVogais(string))

