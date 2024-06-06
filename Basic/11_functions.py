# Functions
# Nos permiten encapsular una logica concreta en un unico lugar
def my_function (order):
    print('This is my '+ order +' function')

my_function ('first')
my_function ('second')

# Funciones con parametros
def sum_two_values (x, y):
    print(x + y)

sum_two_values(8, 10)
sum_two_values(103, 370)

# Funciones con retorno
def sum_two_values_with_return (x, y):
    return x + y

my_result = sum_two_values_with_return (8, 10)
print('El resultado de la funcion => ' + str(my_result))

# Podemos reordenar el orden de los parametros
# Podemos setear valor por defecto a un parametro
def print_name (name, lastname, alias = 'Sin alias'):
    print(name + ' ' + lastname + ' ' + alias)

print_name(lastname = 'Tony', name ='Montana')
print('Mike', 'Miller', 'Mr. 13')

# Funcion con parametros arbitrarios
# Podemos indicar un numero indeterminado de parametros
def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts('Hola', 'Adios', 'Hasta pronto')