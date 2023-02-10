'''Escribe una función que use la función del área del círculo para devolver el volumen de un cilindro, obteniendo por parámetro la longitud del mismo.'''
from math import pi

radio:int = (input('¿Cual es el radio?: '))
areaCirculo:str= (pi*int(radio))**2
print(f'El área del Circulo es {areaCirculo}')

def funcion14():
  longitud: int= (input('¿Cual es la longitud?: '))
  volumenCilindro:int= int(areaCirculo)*int(longitud)
  print(f'El volumen del cilindro es {volumenCilindro}')
funcion14()