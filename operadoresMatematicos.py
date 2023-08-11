from math import ceil, floor

answer = 30 + 12
print(answer)

difference = 30 - 12
print(difference)

product = 30 * 12
print(product)

quotient = 30 / 12
print(quotient)

# divisão somente com numeros inteiros
seconds = 1042
display_minutes = 1042 // 60 # --> essa divisão da 17.3666667
print(display_minutes) # --> vai printar 17

# resto da divisão
display_seconds = 1042 % 60

# Respeitando a ordem das operações matematicas, nos dois casos da 1084
result_1 = 1032 + 26 * 2
result_2 = 1032 + (26 * 2)

# caracteres para numeros
demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

# valor absoluto, mesmo que de negativo ele fica positivo
# pode ser usado por exemplo pra calcular a distância entre dois planetas
print(abs(39 - 16)) # --> 23
print(abs(16 - 39)) # --> 23

# arredondamento
print(round(14.6)) # --> 15

print(round(14.4)) # --> 14

# funcoes da biblioteca
round_up = ceil(12.5)
print(round_up) # --> 13

round_down = floor(12.5)
print(round_down) # --> 12