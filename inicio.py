from datetime import date


def print_hi(name):
    print('Hello Word')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

print("show this in the console")

#   Python é uma linguagem dinamicamente tipada, o que significa que o tipo de variável
# é determinado pelos dados atribuídos a ela

sum = 1 + 2 # 3
product = sum * 2
print(product)

planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string


type = type(distance_to_alpha_centauri) #verificar um tipo

print(type)

left_side = 10
right_side = 5
left_side / right_side # 2

print("Data de hoje convertida para string " + str(date.today()))

print(f'Data de hoje {date.today()}')
