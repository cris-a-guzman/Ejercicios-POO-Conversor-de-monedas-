class Carta:
    def __init__(self, palo, valor) -> None:
        self.palo = palo
        self.valor = valor

    def __getitem__(self, key):
        if key == "palo":
            return f'El palo de la carta es: {self.palo}'
        if key == "valor":
            return f'El valor de la carta es: {self.valor}'
        else:
            return 'Algo salio mal'

    def __str__(self) -> str:
        return f'{self.valor} de {self.palo}'

class Baraja:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.lista_cartas = [[],[],[],[]]

    def agregar_carta(self,carta,palo):
        self.lista_cartas[palo].append(carta)

    def __getitem__(self, palo):
        return self.lista_cartas[palo]

    def __str__(self) -> str:
        resultado = ""
        for i in self.lista_cartas:
            for j in i:
                resultado += f"{j}\n"
        return resultado

