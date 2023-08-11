# Quando você adiciona cadeias de caracteres, o Python não modifica nenhuma cadeia de caracteres,
# mas retorna uma nova cadeia de caracteres como resultado.
# Para manter esse novo resultado, atribua - o a uma nova variável

fact = "The Moon has no atmosphere. "
fact += "No sound can be heard on the Moon."

print(fact)

# pode se usar, aspas simples, duplas ou triplas
# se o meu texto tiver aspas simples, eu uso as duplas, se ele tiver as duplas eu uso as simples


fact2 = 'The "near side" is the part of the Moon that faces the Earth'

fact3 = "We only see about 60% of the Moon's surface"

# se ele tiver simples e duplas eu uso as triplas
fact4 = """We only see about 60% of the Moon's surface, this is known as the "near side"."""

print(fact4)

# quebrar o texto
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

# pode-se obter o mesmo resultado utilizando aspas triplas
multiline2 = """Facts about the Moon:
...  There is no atmosphere.
...  There is no sound."""
print(multiline2)

# titulo
heading = "temperatures and facts about the moon"
print(heading.title())

splitTeste = "teste de espacos"
print(splitTeste.split())

splitTeste2 = "testes,de,virgulas"
print(splitTeste2.split(","))

# importante tomar cuidado com o case sensetive

# contains
contains = "Moon" in "This text will describe facts and challenges with space travel"
print(contains)

# find == indexOf
temperature = "Saturn has a daytime temperature of -170 degrees Celsius"
print(temperature.find("daytime"))
print(temperature.find("teste"))  # retorna -1

# count -- conta quantas vezes uma palavra aparece
print(temperature.count("Celsius"))

print("The Moon And The Earth".lower())

print("The Moon And The Earth".upper())

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)


print("-60".startswith('-'))

print("30 C".endswith("C"))


#join
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
stringJoin = str().join(moon_facts)

print(stringJoin)

# outra forma de interpolar string
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" % mass_percentage)


# utilizando vários valores
print("""Both sides of the %s get the same amount of sunlight,
... but only one side is seen from %s because
... the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

# format
print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))

#{0} == mon e {1} == mass_percentage
print("""You are lighter on the {0}, because on the {0} 
... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))

# uma forma mais legivel é
print("""You are lighter on the {moon}, because on the {moon} 
... you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))

# interpolacao de string
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")

# podemos passar expressoes nas interpolacoes
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")