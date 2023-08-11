def rocket_parts():
    print("payload, propellant, structure")

rocket_parts()

# funcoes podem retornar valor, como essa não retorna, o valor é None
output = rocket_parts()

print(output)

print(output is None)


# funcoes com o mesmo nome
def rocket_parts():
     return "teste, teste, teste"

output = rocket_parts()

print(output)

# passando argumentos para funcao
# se ele tiver algum true, retorna true
any([True, False, False])

# retorna false
any([False, False, False])


# any() --> retorna exception

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"

print(distance_from_earth("Moon"))


def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

days_to_complete(238855, 75)

print("Valor arredondado", round(days_to_complete(238855, 75)))


from datetime import timedelta, datetime

# funcoes com valores padrao
def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

arrival_time_str = arrival_time()

print(arrival_time_str)


# passando parametro
arrival_time_param = arrival_time(0)
print(arrival_time_param)

# passando parametro explicito
arrival_time_param = arrival_time(hours=0)

# usando parametros comuns e default, os default precisam ficar por ultimo
def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

arrival_time_param_str = arrival_time("Moon")
print(arrival_time_param_str)

arrival_time_param_str2 = arrival_time("Orbit", hours=0.13)

arrival_time_param_str2 = arrival_time("Orbit", 0.13)


# recebendo varios parametros -- igual ao Java e c# com ...param
def variable_length(*args):
    print(args)

variable_length("one", "two")

variable_length(None)

variable_length()


#Você pode usar qualquer nome de variável válido. Embora seja comum ver *args ou *a,
# você deve tentar usar a mesma convenção em todos projetos.
def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"


print(sequence_time(4, 14, 18))

print(sequence_time(4, 14, 48))


#recebendo diferentes argumentos com nome
# Você pode usar qualquer nome de variável válido. Embora seja comum ver **kwargs ou **kw,
# você deve tentar usar a mesma convenção em todos projetos.
def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day="Wednesday", pilots=3)

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")


# podem ser passas inumeras palavras chave, porém elas não podem ser repetidas
#crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", pilot="Michael Collins")

crew_members()

def variable_length(teste, **kwargs):
    print(kwargs)
