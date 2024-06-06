# Dictionaries
'''
Un diccionario es una estructura de datos mutable que almacena pares clave-valor, 
donde cada clave es única. Se puede acceder a los valores a través de su clave en
tiempo constante. La sintaxis para crear un diccionario es mediante llaves {} y 
separando cada par clave-valor por dos puntos (:). 

                Por ejemplo: {'nombre': 'Juan', 'edad': 30}.
'''
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {'name':'Tony' , 'lastname':'Montana' , 'age':30 , 1:'M4A1'}
print(my_other_dict)

my_dict = {

    'name':'Tony' ,
    'lastname':'Montana' ,
    'age':30 ,
    'weapons': {'M4A1', 'AK47', 'M16'}

    }

print(my_dict)

# Podemos acceder y modificar al valor usando el nombre de la clave
print(my_dict['weapons'])

my_dict['age'] = 32
print(my_dict['age'])

# Tambien podemos crear nuevos pares clave/valor
my_dict['height'] = 1.78
print(my_dict)

# del nos permite eliminar pares 
del my_dict['weapons']
print(my_dict)

# in permite comprobar si una clave esta en el dict
print('name' in my_dict)

# items() devuelve un listado de los items clave/valor
print(my_dict.items())

# keys() devuelve un listado de las claves
print(my_dict.keys())

# values() devuelve un listado de los valores
print(my_dict.values())

# fromkeys() recibe como parametro las claves y crea un diccionario nuevo 
# Podemos usarlo para crear copias vacias de diccionarios
# Puede recibir un segundo parametro que se repetira como valor para todas las claves
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

