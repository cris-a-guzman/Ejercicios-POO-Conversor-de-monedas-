from clases import Contacto
agenda = Contacto()
def menu():
    print('1 - Agregar contacto\n',
          '2 - Ver contactos\n',
          '3 - Eliminar contactos\n',
          '4 - Salir\n')
    
while True:
    menu()
    user_choice = input('Ingresa el numero de la opcion: ').strip()
    if user_choice == "1":
        key = input('Ingresa el nombre del contacto: ').lower()
        while True:
            numero = input(' Ingresa el numero de telefono del contacto (solo numeros): ').strip()
            if numero.isdigit():
                numero = int(numero)
                break
            else:
                print('Invalido, intentelo de nuevo.')
        agenda[key] = numero
        

    elif user_choice == "2":
        print(agenda)

    elif user_choice == "3":
        print(agenda)
        while True:
            valor = input('Ingresa el nombre del contacto para eliminarlo  o "Q" para salir: ').lower()
            if valor == "q":
                break
            elif valor in agenda.lista.keys():
                agenda.eliminar_contacto(valor)
                break

            else:
                print('No se encontro el contacto, intentelo de nuevo')
    elif user_choice == "4":
        print('Bye...')
        break
    else:
        print('No se encontro la opcion, intentelo de nuevo')