# Dates
from datetime import datetime

# Inicializamos un objeto de tipo datetime
time_now = datetime.now()

# El modulo datetime proporciona clases para trabajar con fechas y horas
time_stamp = time_now.timestamp()
print(time_stamp)

# Requiere 3 parametros obligatorios (year, month, day)
year_2023 =  datetime(2023, 4, 23)

def print_date(date):

    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)

print_date(time_now)
print('=> ')
print_date(year_2023)

# El modulo time proporciona varias funciones relacionadas con el tiempo
# funcionalidad relacionada con datetime y calendar
from datetime import time

# Time crea un objeto que permite encapsular tiempo
current_time = time(21, 6, 10)

print('=> Time ')
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Date sirve para crear un objeto que encapsula fechas
from datetime import date

# .today toma el dia actual y lo guarda en un objeto
# date permite definir una fecha en el formato concreto, igual que time con el tiempo
current_date = date.today()

print('=> Date ')
print(current_date.year)
print(current_date.month)
print(current_date.day)

# Podemos actualizar las fechas almacenadas en un variable volviendo a inicializarlas
current_date = date(current_date.year, current_date.month + 1, current_date.day)
print('New month => ' + str(current_date.month))

# Timedelta nos sirve para trabajar con diferencias entre dos objetos datetime
# suele utilizarse para trabajar con franjas de fechas
from datetime import timedelta

init_timedelta = timedelta(231, 10, 123, weeks=10)
end_timedelta = timedelta(251, 10, 10, weeks=13)

print(end_timedelta - init_timedelta)
print(end_timedelta + init_timedelta)
