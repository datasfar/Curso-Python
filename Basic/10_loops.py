# Loops
# Nos permiten pasar por un mismo codigo varias veces
my_condition = 0

# While recibe una codicion, mientras se cumpla, se ejecuta algo
# Permite el uso de else, ejecuta algo cuando deja de cumplirse. Opcional
while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print('Mi condicion es 10')

print('Hemos salido del bucle while')

# if anidado en while
# break detiene la ejecucion del while 
my_condition = 1
while my_condition < 20:
    my_condition += 2
    if my_condition == 15:
        print('Mi condicion es 15')
        break
    
    print(my_condition)

# For, nos permite recorrer un listado de elementos
print('Bucle for => ')

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_other_dict = {'name':'Tony' , 'lastname':'Montana' , 'age':30 , 1:'M4A1'}

for element in my_other_dict.values():
    print(element)
    if element == 30:
        print('Edad ' + str(element) + ' años')
        # break
        # continue
else:
    print('El bucle ha finalizado => ')