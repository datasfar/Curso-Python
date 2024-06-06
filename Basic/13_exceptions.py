# Exceptions Handling / Manejo de errores

'''
try: 
    {run this code}
except:(can have a condition)
    {execute this code when there is an exception}
else: 
    {No exceptions? Run this code}
finally: 
    {Always run this code}

'''
number_one, number_two = 6, 2
number_two = '2'

# Try / Except
try:
    print(number_one + number_two)
except:
    print('Se ha producido un error')

#  Else y Finally son opcionales
try:
    print(number_one + number_two)
except:
    print('Se ha producido un error')
else:
    # Se ejecuta si no se produce una excepcion
    print('La ejecucion continua correctamente')
finally:
    # Se ejecuta siempre
    print('La ejecucion continua...')

# Excepciones por tipo
# Podemos ejecutar codigo concreto dependiendo del tipo de error
try:
    print(number_one + number_two)
    print('No se ha producido un error')
except ValueError:
    print('Se ha producido un error: ValueError')
except TypeError:
    print('Se ha producido un error: TypeError')

# Captura de la informacion de la excepcion
try:
    print(number_one + number_two)
    print('No se ha producido un error')
except ValueError as error: # Controla 1 tipo de excepcion
    print('Value Error => ' + error)
except Exception  as exception:# Controla cualquier tipo de excepcion 
    print(exception)