# Adaptação de um programa do curriculo do CS50
# Originalmente ele foi escrito em C, esse programa confirma a validade de um cartão de credito
# Além disso, ele fala o nome da companhia de cartão

# pedir um número de cartão
numCartão =  int(input("Número de cartão: "))

# confirmar a entrada dos dados
print(numCartão)

d1 = ((numCartão % 100)/10 * 2)
d2 = ((numCartão % 10000)/1000 * 2)
d3 = ((numCartão % 1000000)/100000 * 2)
d4 = ((numCartão % 100000000)/10000000 * 2)
d5 = ((numCartão % 10000000000)/1000000000 * 2)
d6 = ((numCartão % 1000000000000)/100000000000 * 2)
d7 = ((numCartão % 100000000000000)/10000000000000 * 2)
d8 = ((numCartão % 10000000000000000)/1000000000000000 * 2)

d1 = ((d1 % 100 / 10) + (d1 % 10))
d2 = ((d2 % 100 / 10) + (d2 % 10))
d3 = ((d3 % 100 / 10) + (d3 % 10))
d4 = ((d4 % 100 / 10) + (d4 % 10))
d5 = ((d5 % 100 / 10) + (d5 % 10))
d6 = ((d6 % 100 / 10) + (d6 % 10))
d7 = ((d7 % 100 / 10) + (d7 % 10))
d8 = ((d8 % 100 / 10) + (d8 % 10))

sum1 = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8

d9 = ((numCartão % 10))
d10 = ((numCartão % 1000) / 100)
d11 = ((numCartão % 100000) / 10000)
d12 = ((numCartão % 10000000) / 1000000)
d13 = ((numCartão % 1000000000) / 100000000)
d14 = ((numCartão % 100000000000) / 10000000000)
d15 = ((numCartão % 10000000000000) / 1000000000000)
d16 = ((numCartão % 1000000000000000) / 100000000000000)

sum2 = d9 + d10 + d11 + d12 + d13 + d14 + d15 + d16
sum3 = sum1 + sum2

lenght = 0

visa = numCartão
amex = numCartão 
mastercard = numCartão


if (sum3 % 10) != 0:
    print("INVALID")
    return 0
while numCartão > 0:
    numCartão = numCartão / 10
    lenght+= 1
while visa >= 10:
    visa /= 10
if visa == 4 and lenght == 13 or lenght == 16:
    printf("VISA")
    return 0
    
while amex >= 10000000000000:
    
    amex /= 1000000000000
    
if lenght == 15 and amex == 34 or amex == 37:
    
    print("AMEX")
    return 0
    
 while mastercard >= 100000000000000:
    mastercard /= 100000000000000
    
if lenght == 16 and mastercard >= 51 and mastercard <= 55:
    
    print("MASTERCARD")
    return 0
    
else:
    print("INVALID")
    return 0
