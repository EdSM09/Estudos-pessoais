-- Lua consegue interpretar o tipo da variável somente pelo valor atribuído a ela
-- O nome de uma variável pode começar com um número
-- Por exemplo:


--[[
    Vamos primeiro definir uma variável Nome
    ela armazena um valor "Marcus" que a linguagem interpreta como uma string
]]
Nome = "Marcus"
print(Nome)
print(type(Nome)) -- lembre-se disso


--[[
    Quando o valor da variável anterior é alterado para o num 14
    o tipo da variável é mudado tambem de string --> num
]]
Nome = 14
print(Nome)
print(type(Nome))