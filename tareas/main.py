
#! Registro de Tareas. Crea una clase Tarea que almacene
#! información sobre tareas pendientes. Implementa los
#! métodos __str__ y __len__ para mostrar detalles de la tarea
#! y contar cuántas tareas hay en la lista.

from clases import ListaTareas, Tarea
from eliminar_tarea import eliminar_tarea
from completar_tarea import completar_tarea
tarea1 = Tarea("prueba1", "prueba descripcion", True)
tarea2 = Tarea("prueba2", "prueba descripcion")
tarea3 = Tarea("prueba3", "prueba descripcion", True)
tarea4 = Tarea("prueba4", "prueba descripcion")
tarea5 = Tarea("prueba5", "prueba descripcion")

lista_tareas = ListaTareas("Lista de Tareas")
lista_tareas.agregar_tarea(tarea1)
lista_tareas.agregar_tarea(tarea2)
lista_tareas.agregar_tarea(tarea3)
lista_tareas.agregar_tarea(tarea4)
lista_tareas.agregar_tarea(tarea5)

def menu():
    print(' 1 - Agregar tarea\n',
          '2 - Ver tareas agregadas\n',
          '3 - Eliminar tarea\n',
          '4 - Contar tareas\n',
          '5 - Completar tareas\n'
          '6 - Salir\n')
while True:
    menu()
    user_choice = input(" Ingresa el numero de la opcion: ").strip()

    if user_choice == "1":
        nombre = input(" Ingresa el nombre de la tarea: ")
        descripcion = input(" Ingresa la descripcion de la tarea: ")
        tarea = Tarea(nombre,descripcion)
        lista_tareas.agregar_tarea(tarea)
        
    elif user_choice == "2":
        print(lista_tareas)
    elif user_choice == "3":
        print(lista_tareas)
        indice = input(" Ingresa el numero de la tarea a eliminar: ").strip()
        if indice.isdigit():
            indice = int(indice)-1
            eliminar_tarea(lista_tareas, indice)
        else:
            print(' Lo ingresado no es un numero, intentelo de nuevo.')
    elif user_choice == "4":
        print(f'La cantidad de tareas que hay en la lista es de: {len(lista_tareas)}')
    elif user_choice == "5":

        print(lista_tareas)                                                     #! 
        indice = input(" Ingresa el numero de la tarea a completar: ").strip()   #!
        if indice.isdigit():                                                    #!
            indice = int(indice)-1                                              #! Esto puede ir en una funcion
            completar_tarea(lista_tareas, indice)                               #! Y modularizar
        else:                                                                   #!
            print(' Lo ingresado no es un numero, intentelo de nuevo.')         #!

    elif user_choice == "6":
        break

print(lista_tareas.__str__())