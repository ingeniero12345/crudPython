import random
number = random.randint(1000,9999)
nombre = input('Ingrese nombre: ')
apellido=input('Ingrese apellido: ')
fecha_nacimiento=input('ingrese año de nacimiento: ')
#id_aleatoreo=nombre.upper()[0:2]+apellido.upper()[0:2]+fecha_nacimiento[2:4]+str(number)
id_aleatoreo=f'{nombre.upper()[0:2]+apellido.upper()[0:2]+fecha_nacimiento[2:4]}     {number}'
print(id_aleatoreo)