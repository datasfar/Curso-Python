# Error Types

# SyntaxError
# print 'Hola Python!' # SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print('Hola Python!')

# NameError 
# print(language) # NameError: name 'language' is not defined
language = 'Python'
print(language)

# IndexError
my_list = ['Python', 'Ruby', 'JavaScript']
# print(my_list[4]) # IndexError: list index out of range
print(my_list[0])
print(my_list[1])
print(my_list[2])

# ModuleNotFoundError
# import maths # ModuleNotFoundError: No module named 'maths'
import math

# AttributeError
# print(math.PI) # AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi)

# KeyError
my_dict = {'name':'Tony' , 'lastname':'Montana' , 'age':30 , 1:'M4A1'}
# print(my_dict['color']) # KeyError: 'color'
print(my_dict['name'])
print(my_dict['age'])

# TypeError
# print(my_list['1']) # TypeError: list indices must be integers or slices, not str
print(my_list[1])

# ImportError
# from math import PI # ImportError: cannot import name 'PI' from 'math'
from math import pi
print(pi)

# ValueError
# my_int = int('10 yo') # ValueError: invalid literal for int() with base 10: '10 yo'
my_int = int('10')
print(type(my_int))

# ZeroDivisionError
# print(5/0) # ZeroDivisionError: division by zero
print(5/2)