'''Una tienda vende Discos de música (unos muñecos muy graciosos). Con la idea de vender un stock almacenado durante meses, se decide que discos de género "Black Metal" y "Electro" tienen un descuento del 30%.
Cada disco (usa un diccionario para esto) tendrá:
Nombre
Artista
Año
Precio
Género (solo pueden ser de los siguientes)
Pop
Electro
Reggaeton
Rock
Metal
Death Metal
Black Metal
Escribe un programa que, disponiendo de una lista de discos disponibles en la tienda el usuario pueda elegir el disco a comprar.
Al acabar la compra (pulsando la tecla 0) se deberá mostrar el ticket de compra indicando la fecha de compra (puedes coger la fecha actual a través de datetime), el dinero que se ahorra el usuario y el coste final de la compra.'''

pop={'Nombre': 'Yuju', 'Artista':'Manolo', 'Año': 2000, 'Precio': 4.99, 'Genero': 'pop'}
electro={'Nombre': 'ximpum', 'Artista':'Ricardo', 'Año': 2004, 'Precio': 8.90, 'Genero': 'electro'},
reggeaton={'Nombre': 'mamita', 'Artista':'Benito', 'Año': 2010, 'Precio': 3.60, 'Genero': 'reggeaton'}
rock={'Nombre': 'roll', 'Artista':'Amancio', 'Año': 2002, 'Precio':8.60, 'Genero': 'rock'}
metal={'Nombre': 'hierro', 'Artista':'Pedro', 'Año': 2019, 'Precio':4.60, 'Genero': 'metal'}
deathMetal={'Nombre': 'muerte', 'Artista':'Aldo', 'Año': 2009, 'Precio':9.60, 'Genero': 'deathMetal'}
blackMetal={'Nombre': 'negro', 'Artista':'Fer', 'Año': 2021, 'Precio':8.60, 'Genero': 'blackMetal'}

def sinDescuento():
  cesta = {}
  continuar = True
  while continuar:
    item = input('Introduce el nombre del disco: ')
    precio = float(input('Introduce el precio indicado en pantalla ' + item + ': '))
    cesta[item] = precio
    continuar = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"
  coste = 0
  print('Lista de la compra')
  for item, precio in cesta.items():
    print(item, '\t', precio)
    coste += precio
  print('Coste total: ', coste)
  
def conDescuento():
  cesta = {}
  continuar = True
  while continuar:
    item = input('Introduce el nombre del disco: ')
    precio = float(input('Introduce el precio indicado en pantalla ' + item + ': '))
    cesta[item] = precio*0.3
    continuar = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"
  coste = 0
  print('Lista de la compra')
  for item, precio in cesta.items():
    print(item, '\t', precio)
    coste += precio
  print('Coste total: ', coste)

opcion=''
while opcion != '8':
  if opcion == '1':
    print(pop)
    sinDescuento()
  if opcion == '2':
    print(electro)
    conDescuento()
  if opcion == '3':
    print(reggeaton)
    sinDescuento()
  if opcion == '4':
    print(rock)
    sinDescuento()
  if opcion == '5':
    print(metal)
    sinDescuento()
  if opcion == '6':
    print(deathMetal)
    sinDescuento()
  if opcion == '7':
    print(blackMetal)
    conDescuento() 
  if opcion =='8':
    print(totalTicket)
  opcion = input('Menú de opciones\n(1) Pop (2) electro (3) reggeaton (4) rock (5) metal (6) DeathMetal (7) blackMetal')
      