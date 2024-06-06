# Higher Order Functions / Funciones de orden superior
# Necesitamos importar modulos
from functools import reduce

# Funciones que son capaces de ejecutar funciones o funciones anidadas
def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

# Podemos pasar la funcion como parametro de otra funcion
def sum_two_values_and_add_values(first_value, second_value, function_one):
    return function_one(first_value + second_value) 

print(sum_two_values_and_add_values(19, 3, sum_one))
print(sum_two_values_and_add_values(19, 3, sum_five))

# Closures
'''
las closures son funciones que recuerdan el estado de su entorno al momento de 
su definición, incluso cuando son invocadas en otro contexto. En otras palabras, 
una closure es una función que es capaz de recordar los valores de las variables 
que estaban en su alcance al momento de ser definida, incluso cuando se ejecuta 
en un ámbito diferente.

Las closures son creadas por funciones que devuelven otras funciones. La función 
devuelta es capaz de recordar los valores de las variables de la función que la 
creó, incluso después de que la función original ha dejado de existir.

'''
# Funcion que define una funcion y retorna una funcion
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

# Podmos llamarlas asi =>
add_closure = sum_ten(10)
print(add_closure(10))

# =>
print(sum_ten(10)(10))

# Built-in Higher Order Functions / Funciones de orden superior de Python
numbers = [1, 2, 3, 15, 17, 18]

# Map(), las funciones maps siempre necesitan un conjunto de datos iterable
def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter()
def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce() opera con un valor mas el acumulado, sobre unos valores iterables
def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))

