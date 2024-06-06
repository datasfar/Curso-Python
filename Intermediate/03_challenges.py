# Challenges // Resolucion de Retos


''' 
                - Challenge 0 - FIZZ BUZZ -

 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

'''
# Definimos una función llamada "fizz_buzz" sin parámetros
def fizz_buzz():
    # Iteramos sobre un rango de números del 1 al 100
    for index in range(1, 101):
        # Si el número es divisible entre 3 y 5, imprimimos "fizzbuzz"
        if index % 3 == 0 and index % 5 == 0:
            print('fizzbuzz')
        # Si el número es divisible entre 3, imprimimos "fizz"
        elif index % 3 == 0:
            print('fizz')
        # Si el número es divisible entre 5, imprimimos "buzz"
        elif index % 5 == 0:
            print('buzz')
        # Si el número no es divisible entre 3 o 5, imprimimos el número
        else:
            print(index)
            
# Llamamos a la función "fizz_buzz" para ejecutarla
fizz_buzz()


''' 
                - Challenge 1 - ES UN ANAGRAMA ? -

 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.

'''
# Funcion que comprueba si dos strings son anagramas
def is_anagram(str_one, str_two):
    
    # Convierte ambas cadenas a minúsculas
    str_one = str_one.lower()
    str_two = str_two.lower()
    
    # Comprueba si las cadenas son idénticas, en cuyo caso no pueden ser anagramas
    if str_one == str_two:
        return False

    # Si las cadenas no son iguales, ordena ambas y comprueba si son iguales
    return sorted(str_one) == sorted(str_two)

# Llamamos a la funcion con un ejemplo
print(is_anagram('amor','roma'))


''' 
                - Challenge 2 - SUCESION FIBONACCI -

 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...

'''
# Funcion que imprime los 50 primero valores de fibonacci
def fibonacci(n):

    # Creamos dos variables que corresponderan al numero anterior y al siguiente
    prev, next = 0, 1

    # Recorremos un rango 
    # Usamos una variable _ para el índice del bucle for, ya que no se usa en el bucle
    for _ in range(n):

        # Imprimimos prev
        print(prev)

        # Actualizamos los valores
        prev, next = next, prev + next

# Llamamos a la funcion 
fibonacci(50)

''' 
                - Challenge 3 - ES NUMERO PRIMO? -

 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.

'''
# Función que comprueba si un número es primo e imprime los números primos entre 1 y 100.
def is_prime(number):
    
    # Iteramos a través de los números del 1 al 100.
    for number in range(1, 101):
        
        # Comprobamos si el número es mayor o igual que 2 (ya que los números primos son mayores o iguales a 2).
        if number >= 2:
            
            # Inicializamos una variable is_divisible en Falso.
            is_divisible = False
            
            # Comprobamos si el número es divisible por algún número entre 2 y el número - 1.
            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break
            
            # Si el número no es divisible por ningún número entre 2 y el número - 1, lo imprimimos (ya que es un número primo).
            if not is_divisible:       
                print(number)

# Llamamos a la función con un número cualquiera (en este caso, 8).
is_prime(8)

''' 
                - Challenge 4 - INVIRTIENDO CADENAS -

 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

'''
# Se define una función llamada reverse que toma un parámetro de texto
def reverse(text):
    # Se obtiene la longitud del texto
    text_len = len(text)
    # Se define una variable llamada reversed_text como una cadena vacía
    reversed_text = ''

    # Se utiliza un bucle for para recorrer cada letra del texto
    # Se comienza desde 0 y se llega hasta text_len - 1
    for index in range (0, text_len):
        # Se agrega la letra del texto en la posición index a la variable reversed_text
        # Pero se toma la letra desde el final del texto restando index y 1
        reversed_text += text[text_len - index -1]

    # Se retorna la cadena de texto invertida
    return reversed_text

# Se llama a la función reverse con el parámetro 'Hola Mundo' y se imprime el resultado
print(reverse('Whats up?'))