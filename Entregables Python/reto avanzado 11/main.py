'''Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:
NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean)
El programa debe mostrar las siguientes opciones para que escoja el usuario:
(1) Añadir un cliente
(2) Eliminar cliente por NIF
(3) Mostrar Cliente por NIF
(4) Listar TODOS los clientes
(5) Mostrar ÚNICAMENTE los clientes preferentes
(6) Finalizar Programa'''

carteraClientes = {}
opcion = ''
while opcion != '6':
    if opcion == '1':
      nif:str = input('Indique el NIF del cliente: ')
      nombre:str = input('Indique el nombre del cliente: ')
      apellido:str = input('Indique los apellidos del cliente: ')
      telefono:str = input('Indique el teléfono del cliente: ')
      email:str = input('Indique el email del cliente: ')
      preferente:bool = input('¿Es un cliente preferente? ')
      cliente={'nombre': nombre,'apellido': apellido, 'telefono': telefono, 'email': email,'preferente': preferente}
      carteraClientes[nif]=cliente
    
    if opcion == '2':
        nif = input('Introduce NIF del cliente que desea eliminar: ')
        if nif in carteraClientes:
            del carteraClientes[nif]
        else:
            print('El NIF que indica no pertenece a ninguno de nuestros clientes', nif)
          
    if opcion == '3':
        nif = input('Introduce NIF del cliente que desea consultar: ')
        if nif in carteraClientes:
            print('NIF:', nif)
            for clave, valor in carteraClientes[nif].items():
                print(clave.title() + ':', valor)
        else:
            print('NEl NIF que indica no pertenece a ninguno de nuestros clientes', nif)
          
    if opcion == '4':
        print('Lista de clientes')
        for clave, valor in carteraClientes.items():
            print(clave, valor['nombre'])
          
    if opcion == '5':
        print('Lista de clientes preferentes')
        for clave, valor in carteraClientes.items():
            if valor['preferente']:
                print(clave, valor['nombre'])
              
    opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')
