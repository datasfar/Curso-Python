# Lists
# Listas (son parecidas a los arrays pero con mas funcionalidad)
# Las listas son estructuras de almacenamiento de datos
my_list = list()
my_other_list = []

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

# Podemos guardar diferentes tipos de datos en las listas
my_other_list = [35, 1.77, 'Tony', 'Montana']
print(type(my_other_list))

# Podemos crear varias variables a la vez igualandolas a la tupla
# Desempaquetado de elementos
age, height, name, lastname = my_other_list
age, height, name, lastname = my_other_list[0], my_other_list[1], my_other_list[2], my_other_list[3]
print(age, height, name, lastname)


# Podemos acceder a los datos guardados en las listas usando index
print(my_other_list[0])
print(my_other_list[3])

# Con los numeros en negativo, empezamos a contar por el final
print(my_other_list[-1])

# count() recibe un parametro y devuelve el numero de ocurrencias de un valor (las veces que se repite)
print(my_list.count(30))

# append() recibe un parametro y lo inserta al final de la lista
my_other_list.append('Miami')
print(my_other_list)

# insert() recibe el indice y la posicion en la que lo inserta
my_other_list.insert(1, 'M4A1')
print(my_other_list)

# remove() recibe un parametro y elimina el primer elemento igual
my_other_list.remove('M4A1')
print(my_other_list)

# pop() elimina el ultimo elemento de la lista y devuelve el valor 
# Puede recibir un parametro que sera el indice del elemento a borrar
print(my_other_list.pop())
my_other_list.pop()
print(my_other_list)

# copy() copia una lista 
my_other_list2 = my_other_list.copy()
print(my_other_list2)

# clear() borra la lista
my_other_list2.clear()
print(my_other_list2)

# reverse() cambia el orden de los elementos a la inversa
my_other_list.reverse()
print(my_other_list)

# sort() ordena una lista
my_list.sort()
print(my_list)

# Tambien podemos crear lista si conocemos los indices de la misma forma que usabamos slice() con strings
print(my_other_list[1:3])
