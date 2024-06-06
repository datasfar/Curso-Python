# List Comprehension
'''
La List Comprehension es una sintaxis de Python para crear listas de manera concisa 
y eficiente a partir de una expresión y una o más iteraciones. Permite generar una 
lista de manera más clara y fácil de leer que utilizando ciclos for y condicionales.

'''

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_original_list)

# Podemos crear una lista a partir de un rango
my_range = range(10)
print(list(my_range))

# Se crea una lista a partir de un bucle que recive un rango
# Estamos iterando sobre la lista al momento de crearla
my_list = [i + 1 for i in range(10)]
print(my_list)

my_list = [i * 2 for i in range(10)]
print(my_list)

my_list = [i * i for i in range(10)]
print(my_list)

# Ofrece multiples opciones
def sum_five(n):
    return n + 5        


my_list = [sum_five(i) for i in range(10)]
print(my_list)


