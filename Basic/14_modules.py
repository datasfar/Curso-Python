# Modules / import nos permite acceder a otros ficheros
# el nombre de los ficheros para modulos usa una sintaxis concreta
import module

# Podemos importar funciones concretas con from module_name import function_name
# from module import sum_values, print_values
# sum(3,4,4) Al importar funciones concretas, no necesitamos llamar al fichero cada vez

# Hay que especificar el modulo para acceder a su contenido
module.sum_values(5, 3, 8)
module.print_values('Hola Python!')

# Modulos de propios de Python
# Python tiene modulos especificos que podemos decidir importar o no
import math

print(math.pi)
print(math.pow(2, 8))