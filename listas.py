planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

# tamanho da lista
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

# adicionando valores a lista
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

# removendo o ultimo elemento
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

# removendo elemento com index
planets.pop(5)  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

# indices negativos
# No exemplo a seguir, o índice -1 retorna o último item da lista. O índice -2 retorna o penúltimo item da lista.
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

# encontrando index, caso não encontre é retornado -1
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

bus_weight = 12650  # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "kg")

# Output
# On Earth, a double-decker bus weighs 12650 kg
# On Mercury, a double-decker bus weighs 4781.7 kg


bus_weight = 12650  # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")

# Output
# On Earth, a double-decker bus weighs 12650 kg
# The lightest a bus would be in the solar system is 4781.7 kg
# The heaviest a bus would be in the solar system is 29854 kg


# Você pode extrair parte de uma lista usando uma fatia. A fatia usa colchetes, mas em vez de conter apenas um item
# ela tem os índices inicial e final da fatia. Ao usar uma fatia, você cria uma lista que começa no índice inicial e
# termina imediatamente antes do índice final (não inclui ele).

# A lista de planetas tem oito itens. A terra é a terceira da lista.
# Para obter os planetas antes da terra, use uma fatia para obter os itens começando em 0 e terminando em 2:


planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)

# Output: ['Mercury', 'Venus']

planets_after_earth = planets[3:7]
print(planets_after_earth)

# Output
# ['Mars', 'Jupiter', 'Saturn', 'Uranus']


planets_after_earth = planets[3:]
print(planets_after_earth)

# Output
# ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


# unindo listas
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output The regular satellite moons of Jupiter are ['Metis', 'Adrastea', 'Amalthea', 'Thebe', 'Io', 'Europa',
# 'Ganymede', 'Callisto']

print("----------- ", "Metis" in amalthea_group)

objects_list = [{
    "description": "teste"
},
    {
        "description": "teste2"
    }]

print("object in list ", "description" in objects_list[0])

# classificando listas
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output The regular satellite moons of Jupiter are ['Adrastea', 'Amalthea', 'Callisto', 'Europa', 'Ganymede', 'Io',
# 'Metis', 'Thebe']

regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)


# Output The regular satellite moons of Jupiter are ['Thebe', 'Metis', 'Io', 'Ganymede', 'Europa', 'Callisto',
# 'Amalthea', 'Adrastea']


def get_reason(response_object, default_message):
    if isinstance(response_object, list) and "description" in response_object[0]:
        return response_object[0]["description"]

    return default_message


response_obj1 = {}
response_obj = [{
    "description": "retorno description"
}]
default_message = "return test"

print("This text is returned by get_reason method ", get_reason(response_obj, default_message))
