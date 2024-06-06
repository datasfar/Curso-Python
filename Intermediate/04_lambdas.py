# Lambdas
# Las lambdas son funciones anonimas (no tienen nombre) que se pueden crear en 
# una sola línea de código. Las lambdas se pueden almacenar en variables.
sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(4, 9))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(3, 5))

# Podemos usar lambdas dentro de una funcion
def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(4, 6))

