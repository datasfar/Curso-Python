# Tuples
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.80, 'Mike', 'Myller')
my_other_tuple = (40, 1.83, 'Bruce', 'Banner')
print(my_tuple)
print(my_tuple[1])
print(type(my_tuple))  

# Las tuples son inmutables, no permite reasignar valores
# my_tuple[1] = 1.90  TypeError: 'tuple' object does not support item assignment
my_new_tuple = my_tuple + my_other_tuple
print(my_new_tuple)

# Las tuples permiten el uso de slicers
print(my_new_tuple[1:6])

# count() cuenta el numero de valores iguales y retorna un int
print(my_tuple.count('Mike'))

# index() recibe un parametro y retorna el indice del primer valor que encuentre
print(my_tuple.index('Mike'))

# Si queremos que los valores de una tuple sean mutables, tendriamos que usar listas en su lugar
my_tuple = list(my_tuple)
print(type(my_tuple))
my_tuple[0] = 39
print(my_tuple)

# del elimina la tupla (funciona con cualquier tipo de dato)
del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined 