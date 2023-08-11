

planet = {
    'name': 'Earth',
    'moons': 1
}

# Capturando o valor -- Displays Earth
print(planet.get('name'))
print(planet['name'])

wibble = planet.get('wibble') # Returns None
# wibble = planet['wibble'] # Throws KeyError


# modificando valores
planet.update({'name': 'Makemake'})

planet['name'] = 'Makemake'

print(planet.get('name'))


# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79


# adicionando uma nova key
planet['orbital period'] = 4333

# removendo uma key
planet.pop('orbital period')


# adicionando um dicionario dentro de outro
# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }

# pegando os valores de um dicionario
print(f"{planet['name']} polar diameter: {planet['diameter (km)']['polar']}")

print(f"{planet.get('name')} polar diameter: {planet.get('diameter (km)').get('polar')}")

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

# pegando as keys
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

# Output:
# october: 3.5cm
# november: 4.2cm
# december: 2.1cm

# criando ou atualizando um valor em um dicionario
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1


# pegando os values
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter')

# Output:
# There was 10.8cm in the last quarter