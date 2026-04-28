# Conversor de Monedas. Crea una clase Moneda que
# permita la conversión entre monedas (ej. dólares a pesos).
# Implementa los métodos __str__ y __add__ para mostrar la
# cantidad convertida y sumar cantidades en diferentes
# monedas.

from monedas import Moneda
from agregar_moneda import agregar_moneda
from convertir_monedas import convertir_monedas
from sumar_monedas import sumar_monedas
from ver_monedas import ver_monedas
from eliminar_monedas import eliminar_monedas

monedas = []

peso = Moneda("Peso", 150000, 0.00071)
dollar = Moneda("USD", 1000,1)
yuan = Moneda("Yuan", 4500, 0.15)
real = Moneda("Real", 3000, 0.20)
monedas.append(peso)
monedas.append(dollar)
monedas.append(yuan)
monedas.append(real)

def menu():
    print(' 1 - Agregar Moneda\n',
          '2 - Ver monedas agregadas\n',
          '3 - Convertir monedas a usd\n',
          '4 - Sumar monedas\n',
          '5 - Eliminar monedas\n',
          '6 - Salir')

print(f'Programa de conversion de Monedas')


while True:
    menu()
    user_choice = input(" Ingresa el numero de la opcion: ").strip()

    if user_choice == "1":
        nombre, cantidad, tasa_usd = agregar_moneda()
        moneda = Moneda(nombre,cantidad,tasa_usd)
        monedas.append(moneda)
    elif user_choice == "2":
        ver_monedas(monedas)
    elif user_choice == "3":
        ver_monedas(monedas)
        while True:
            eleccion = input(' Ingresa el numero de la moneda que queres convertir a USD: ')
            if eleccion.isdigit():
                eleccion = int(eleccion)
                break
            else:
                print(' Lo ingresado no es un numero, intentelo de nuevo.')
        convertir_monedas(monedas[eleccion-1], monedas)

    elif user_choice == "4":
        ver_monedas(monedas)
        elegidas = []
        while True:
            moneda = input(' Ingresa el numero de la moneda para sumar (ingrese q para terminar de elegir):').lower().strip()
            if moneda.isdigit():
                moneda = int(moneda)-1
                if 0<=moneda<len(monedas):
                    elegidas.append(monedas[moneda])
                elif moneda in elegidas:
                    print('Ya haz elegido esta moneda')
                else:
                    print(' No se encontro la moneda elegida')
            elif moneda == "q":
                break
        sumar_monedas(*elegidas)
    elif user_choice == "5":
        ver_monedas(monedas)
        moneda = input(' Ingresa el numero de la moneda a eliminar: ')
        if moneda.isdigit():
            moneda = int(moneda)-1
            if 0<=moneda<len(monedas): #! Aca no usamos ninguna funcion ni esta modularizado.
                eliminada = monedas.pop(moneda)
                print(f'Moneda eliminada: {eliminada}')
                ver_monedas(monedas)
            else:
                print(' No se encontro la moneda elegida.')
        else:
            print(' Lo ingresado no corresponde a una opcion')
    elif user_choice == "6":
        break


