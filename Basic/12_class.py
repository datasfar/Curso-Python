# Class
class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

# Constructor de clase
class Person:
    # Creamos variables
    def __init__(self, name, lastname, alias = 'Sin alias'):
        self.name = name
        self.lastname = lastname
        self.fullname = name + ' ' + lastname
        # Podemos definir variables privadas con (__) antes del nombre de la variable
        self.__alias = alias

    # Para acceder a propiedades privadas debemos usar funciones (funciona como un get en otros lenguages)    
    def get_alias(self):
        return self.__alias
    
    # Creamos funciones
    def walk(self):
        print(f'{self.fullname} Esta caminando')

# Creamos nueva instancia del objeto
my_person = Person('Mike', 'Miller')
print(my_person.fullname)
my_person.walk()

my_other_person = Person('Bruce','Vanner', 'Hulk')
print(my_other_person.get_alias())