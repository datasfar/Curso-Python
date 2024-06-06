# Las variables en python utilizan la nomenclatura snake_case
my_variable = 'My string variable'
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# Declarar multiples variables en una sola linea (no es buena practica)
first_name, last_name, age = 'Tony', 'Montana', 37
print(first_name, last_name, age)

# print() puede tomar multiples argumentos
print('Variables:', my_variable, my_int_variable, my_bool_variable)

# str() modifica el tipo de una variable a string
# int() modifica el tipo de una variable a integer
# Existen muchos mas modificadores como: float(), bool()...
my_int = 1
print(type(my_int))

my_int_to_string = str(my_int)
print(type(my_int_to_string))

my_string_to_int = int(my_int_to_string)
print(type(my_string_to_int)) 

# len() cuenta caracteres
print(len(my_variable))

# input() permite la insercion de codigo desde consola
name = input('What is your name? ')
lastname = input('What is your lastname? ')
print('Hello', name, lastname)

# Python no permite la creacion de constantes
# Para indicar que una variable es variable final, la definiremos en mayus
CONST_NAME = 'Name'
