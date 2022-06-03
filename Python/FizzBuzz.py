# versão do desafio FizzBuzz para python
#  se o numero entre 1 e 100 for divisivel por 3 e 5
#       imprima fizzbuzz
#  se o número for divisivel por 3
#      imprima fizz
#  se o numero dor divisivel por 5 
#       imprima buzz
#  se nenhuma delas for satisfeita 
#       imprima o número 


#lembre-se que o python não usa chaves para a endentação
# e que essa linguagem é bem mais literal do que outras
for i in range(0, 101):
        if i % 3 == 0 and i % 5== 0:
                print("FizzBuzz")
        elif i% 5 ==0:
                print("Fizz")
        elif i%3 == 0:
            
                print("Buzz") 
        else:
            print(i)  
    
