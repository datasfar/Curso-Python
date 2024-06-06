# Strings
my_string = 'Mi string'
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = 'Esto es un string \n con salto de linea'
print(my_new_line_string)

my_new_tab_string = '\t Esto es un string con tabulacion'
print(my_new_tab_string)

my_scape_string = '\\t Esto es un string \\n escapado con (\)'
print(my_scape_string)

# Formateo
# Usando {} devolvemos el objeto respetando el tipo
name, lastname, age = 'Tony', 'Montana', 37
print('Mi nombre es {} {} y mi edad es {}'.format(name, lastname, age))

# Inferencia de datos (f) antes del string y el {nombre_de_la_variable} 
print(f'Mi nombre es {name} {lastname} y mi edad es {age}')

# Se usa %s para strings y %d para numeros
print('Mi nombre es %s %s y mi edad es %d'%(name, lastname, age))

# Desempaquetado de caracteres
language = 'Python'
a, b, c, d, e, f = language
print(c)
print(f)

# Division
# slice recorta parte del string y la devuelve [inicio, fin(no incluido)] 
# La indexacion comienza con 0
language_slice = language[1:3]
print(language_slice)

# Si no tiene fin, coge hasta el final
language_slice = language[1:]
print(language_slice)

# Con numeros negativos, comienza por el final
language_slice = language[-3]
print(language_slice)

# Coge un rango y salta x numeros
language_slice = language[0:6:2]
print(language_slice)

# Con [::-1] podemos invertir el string
reversed_language = language[::-1]
print(reversed_language)

# Funciones
# capitalize() pone la primera letra en mayuscula
brand = 'nestle'
print(brand.capitalize())

# upper() pasa toda la cadena a mayusculas
print(brand.upper())

# lower() pasa toda la cadena a minusculas
print(brand.lower())

# count('x') cuenta todas las x en el string, retorna un int
print(brand.count('e'))

# isnumeric() devuelve un boolean con la comprobacion de si es un numero
# isupper() comprueba si la cadena esta en mayus
# islower() comprueba si la cadena esta en minus
print(brand.isnumeric())
print(brand.isupper())
print(brand.islower())

# startswith('x') comprueba si la cadena comienza con el valor dado
print(brand.startswith('nes'))