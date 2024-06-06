# RegExp Regular Expresions / Expresiones Regulares
# Con las regex podemos comprobar si existen ciertas cosas dentro de una cadena

import re # Modulo de las expresiones regulares

my_string = 'Esta es la leccion numero 8: Leccion Expresiones Regulares'
my_other_string = 'Esta no es la leccion numero 7: Manejo de Ficheros'

print(re.match('Esta es la leccion', my_string))
print(re.match('Esta es la leccion', my_other_string))

# Devuelve None porque match empieza a buscar desde el principio de la cadena
print(re.match('Expresiones Regulares', my_string)) 

# 
match = re.match('Esta es la leccion', my_string, re.I) #re.I regex del sistema (flags) I = ignore case
print(match)

# Devuelve el rango en el que coinciden los caracteres (n, n)
span = match.span()
print(span)
# Almacenamos en variables el contenido de span
start, end = span
# Ya podriamos imprimirlo
print(my_string[start:end])

# Search
search = re.search('Esta es la leccion', my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# Findall
# Devuelve un listado con las veces que lo ha encontrado
find_all = re.findall('Esta es la leccion', my_string, re.I)
print(find_all)

find_all = re.findall('e', my_string, re.I)
print(find_all)

# Split
# Busca un patron y divide a partir de el
split = re.split('a', my_string)
print(split)

# Sub
# Sustituimos el primer argumento por el segundo en el string dado
sub = re.sub('Expresiones', 'expresiones', my_string)
print(sub)
# Podemos dar mas de un parametro como primer argumento usando |
sub = re.sub('a|e|E|i|u', 'o', my_string)
print(sub)
#[L|l]eccion => Tambien funcionaria

# Patterns / Patrones
'''
[]: A set of characters
[a-c] means, a or b or c
[a-z] means, any letter from a to z
[A-Z] means, any character from A to Z
[0-3] means, 0 or 1 or 2 or 3
[0-9] means any number from 0 to 9
[A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
\: uses to escape special characters
\d means: match where the string contains digits (numbers from 0-9)
\D means: match where the string does not contain digits
. : any character except new line character(\n)
^: starts with
r'^substring' eg r'^love', a sentence that starts with a word love
r'[^abc] means not a, not b, not c.
$: ends with
r'substring$' eg r'love$', sentence that ends with a word love
*: zero or more times
r'[a]*' means a optional or it can occur many times.
+: one or more times
r'[a]+' means at least once (or more)
?: zero or one time
r'[a]?' means zero times or once
{3}: Exactly 3 characters
{3,}: At least 3 characters
{3,8}: 3 to 8 characters
|: Either or
r'apple|banana' means either apple or a banana
(): Capture and group
'''

# Ejemplos:
# Con la r podemos crear expresiones regulares
pattern = r'[lL]eccion'
print(re.findall(pattern, my_string))

pattern = r'[lL]eccion|Expresiones'
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r'[a-z]' # Letras de a a z
print(re.findall(pattern, my_string))

pattern = r'[0-9]' # Numeros del 0 al 9
print(re.findall(pattern, my_string))

pattern = r'\d' # Solo numeros
print(re.findall(pattern, my_string))

pattern = r'\D' # Solo letras
print(re.findall(pattern, my_string))

pattern = r'[l].' # l seguido de un caracter
print(re.findall(pattern, my_string))


# Patron de validacion de email
email = 'Mymail@mail.com'
fake_email = 'Mymail@mail.m'

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

print(re.findall(pattern, fake_email))


