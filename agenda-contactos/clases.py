
class Contacto:
    def __init__(self) -> None:
        self.lista = {}

    def __setitem__(self, key, value):
        self.lista[key] = value
        print(f'Guardando el contacto {key} con el numero: {value}')

    def eliminar_contacto(self, key):
        print(f'Eliminando el Contacto "{key}" | Numero: {self.lista[key]}')
        self.lista.pop(key)
    
    def __str__(self) -> str:
        resultado = ""
        for key,value in self.lista.items():
            resultado += f"Nombre: {key} | Numero: {value}\n"
        if resultado:
            return resultado
        else:
            return 'No hay contactos guardados todavia'