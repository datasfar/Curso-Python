# Python Package Manager / Gestor de paquetes para python
# pip / Python Package Index / https://pypi.org

# Me esta dando problemas porque parece que no esta en PATH (check this out!)

# Terminal
# pip --version / comprobar version de pip # 22.3.1
# pip install --upgrade pip / actualizar a ultima version 
# pip install (packagename) / instala un paquete 

#pip install numpy 
#pip install pandas

# Una vez instalado e importado
import numpy
# Ya tendremos acceso al modulo
print(numpy.version.version)
numpy_array = numpy.array([32, 45, 12, 12, 56, 32, 54, 67])
print(numpy_array * 2)

# pip list, muestra un listado de las librerias instaladas
# pip unistall pandas, permite eliminar paquetes
# pip show numpy, devuelve informacion del modulo

# pip install request (permite hacer peticiones a una API)
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response.json())

# Paquetes propios
from my_package import arithmetics
print(arithmetics.sum(2,4))

'''
            / Algunas Libreriras Interesantes / 
numPy => NumPy es una librería en Python para cálculo numérico y científico que permite 
trabajar de manera eficiente con matrices, vectores y operaciones matemáticas, especialmente 
para grandes conjuntos de datos. También ofrece funciones estadísticas y de visualización de 
datos mediante la integración con Matplotlib.

pandas => Pandas es una librería en Python para manipular y analizar datos de manera eficiente 
y flexible. Con Pandas, se pueden trabajar con datos tabulares, importar y exportar datos en 
varios formatos, limpiar y preprocesar los datos, realizar operaciones estadísticas y visualizar 
datos.

requests => Requests es una librería en Python para enviar solicitudes HTTP/1.1 y manejar la respuesta 
del servidor. Con Requests, se pueden realizar solicitudes GET, POST, PUT, DELETE, HEAD y otras, enviar 
datos con las solicitudes, manejar la autenticación y cookies de sesión, y enviar solicitudes seguras 
a través de SSL. 
'''