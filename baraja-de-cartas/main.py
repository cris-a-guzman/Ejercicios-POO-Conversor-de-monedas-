from clases import Carta, Baraja
import random
baraja = Baraja("baraja de cartas")
palos = ['Basto', 'Copa', 'Espada', 'Oro']
for i in range(1,5):
    for j in range(1,13):
        carta = Carta(palos[i-1],j)
        baraja.agregar_carta(carta,i-1)
def menu():
    print('1 - Ver cartas\n',
          '2 - Consultar carta random\n',
          '3 - Consultar carta a eleccion\n',
          '4 - Salir\n')
    
while True:
    menu()
    user_choice = input(' Ingresa el numero de la opcion: ').strip()
    if user_choice == "1":
        print(baraja)
    elif user_choice == "2":
        palo = random.randint(0,3)
        numero = random.randint(0,11)
        carta = baraja[palo]
        print(carta[numero])
    elif user_choice =="3":
        for i,valor in enumerate(palos):
            print(f'{i+1} - {valor}')
        while True:
            palo = input(' Ingresa el numero del palo: ')
            if palo.isdigit():
                palo = int(palo)-1
                if 0<=palo<=len(palos):
                    break
                else:
                    print('El numero seleccionado no corresponde a un palo, intentelo de nuevo.')
            else:
                print('Lo ingresado no corresponde a ningun palo, intentelo de nuevo.')
        while True:
            numero = input(' Ingresa el numero de la carta (de 1 - 12)').strip()
            if numero.isdigit():
                numero = int(numero)-1
                if 0<=numero<=11:
                    break
                else:
                    print('Lo ingresado no corresponde a un valor correcto, intentelo de nuevo')
            else:
                print('Lo ingresado no corresponde a un valor correcto, intentelo de nuevo')

        carta = baraja[palo]
        print(carta[numero])
    elif user_choice == "4":
        print('Bye...')
        break
    else:
        print(' Lo ingresado no corresponde a una opcion, intentelo de nuevo.')