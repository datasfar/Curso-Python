# Coditionals 
my_condition = True

# if, si se cumple una condicion ejecuta un codigo
if my_condition:
    print('Se cumple la condicion 1')

print('La ejecucion continua')

my_condition = 5 * 2
if my_condition > 9:
    print('my_condition es mayor a 9')
else:
    print('my_condition no cumple la condicion')   

# Podemos usar operadores logicos para pasar varias condiciones
if my_condition > 9 and my_condition <20 :
    print('my_condition es mayor a 9 y menor que 20')
elif my_condition == 21:
    print('su cumple el elif(else if)')
else:
    print('my_condition no cumple la condicion')   

# Las variables vacias se computan como false
my_string = ''
if my_string:
    print('el string es true')
else:
    print('el string es false')