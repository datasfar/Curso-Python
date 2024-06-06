# File Handling / Manejo de fichereos

# .txt file
import os
txt_file = open('Intermediate/my_file.txt', 'w+') #r+ lectura y escritura w+ sobreescribe
# Despues de cada orden el puntero se queda donde este, no vuelve al principio
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())

# Escribimos datos en el fichero
txt_file.write('Primera Linea \n Segunda Linea \n Esto es una line agregada desde python') 

# En este caso no funciona porque tras escribir el puntero esta al final y lee desde ahi
for line in txt_file.readlines(): # Podemos iterar y leer cada fila
    print(line)

txt_file.close() #Cerramos el fichero
#os.remove('Intermediate/my_file.txt')

# .json file
import json

# Creamos el fichero
json_file = open('Intermediate/my_file.json', 'w+')

# Creamos el objeto
json_test = {
    'name':'Tony',
    'lastname':'Montana', 
    'age':30, 
    '1':'M4A1',
    'languages': ['english', 'spanish', 'french']}

# Dumpeamos el objeto el el fichero
json.dump(json_test, json_file, indent = 2)

# Cerramos el archivo
json_file.close()

# Volvemos a abrirlo, lo que nos coloca el cursor al inicio del fichero
with open('Intermediate/my_file.json') as my_other_file:
    for line in my_other_file.readlines(): # Podemos iterar y leer cada fila
        print(line)

json_dict = json.load(open('Intermediate/my_file.json'))
print(type(json_dict))

# .csv file
import csv

csv_file = open('Intermediate/my_file.csv', 'w+')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['name', 'lastname', 'location', 'age', 'language'])
csv_writer.writerow(['Tony', 'Montana', 'Miami', '34', 'English'])
csv_writer.writerow(['Frank', 'Sosa', 'Bolivia', '40', 'Spanish'])

csv_file.close()

with open('Intermediate/my_file.csv') as my_other_file:
    for line in my_other_file.readlines(): # Podemos iterar y leer cada fila
        print(line)

# .xlsx file import xlrd # Debe instalarse el modulo

# .xml file
import xml