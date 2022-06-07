-- Vou somente explorar alguns tipos na linguagem
-- lembrete: Lua não faz distinção entre floats ints longs etc todos eles são do tipo num


-- lua tem uma boa precisãoo com relação a numeros do tipo float
Var1 = 1.999999999999 + 0.0000000000001
print(Var1)
io.write(type(Var1))