'''Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.'''
def funcion13_1 ():
  base= int(input('¿Cual es la base del triangulo?: '))
  altura= int(input('¿Cual es la altura del triangulo?: '))
  areaTriangulo= int(base)* int (altura) / 2
  print(f'El área del tiangulo es: {areaTriangulo}')
  
from math import pi
def funcion13_2 ()->int:
  radio:int = (input('¿Cual es el radio?: '))
  areaCirculo:str= (pi*int(radio))**2
  print(f'El área del Circulo es {areaCirculo}')

funcion13_1()
funcion13_2()