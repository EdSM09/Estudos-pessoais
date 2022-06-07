-- Vou somente explorar alguns tipos na linguagem
-- lembrete: Lua não faz distinção entre floats ints longs etc todos eles são do tipo num


-- lua tem uma boa precisãoo com relação a numeros do tipo float
Var1 = 1.999999999999 + 0.0000000000001
print(Var1)
print(type(Var1))

Var2 = [[
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec non interdum risus.
Vivamus gravida tortor vitae diam convallis commodo. 
Nulla cursus sapien ac eros fringilla laoreet.
]]
print(Var2)

Var3 = true
print(Var3)
print(type(Var3))