# Sets
# Un set NO es una estructura ordenada, utiliza un hash para guardar todos los elementos
# Un set no admite repetidos, ni acceso por indice
my_set = set()
my_other_set = {}

print(type(my_set))

print(type(my_other_set)) # Inicialmente es un diccionario
my_other_set = {'Frank', 'Saliery', 29} # Al agregar datos se transforma en un set
my_set = my_other_set.copy()

print(my_other_set)
print(type(my_other_set))
print(len(my_other_set))

# add() recibe un argumento y lo inserta 
my_other_set.add('Mafia 1')
print(my_other_set)

# in permite comprobar si un elemento existe en un set, devuelve un bool
print('Saliery' in my_other_set)
print('Montana' in my_other_set)

# clear() elimina el contenido del set
my_other_set.clear()
print(my_other_set)

# Podemos cambiar el type usando el constructor (list() por ejemplo)
print(type(my_set))

# Ahora tenemos una estructura de datos ordenada. OJO: seguimos sin saber el orden
my_list = list(my_set)
print(my_list[0])

# union() permite unir sets
set_one = {'Scarface', 'The Godfather', 'Gangster Squad'}
set_two = {'22 bullets', 'The inmortal', 'American Ganster'}

set_three = set_one.union(set_two)
print(set_three)

# difference() devuelve los valores que no coinciden
print(set_three.difference(set_two))