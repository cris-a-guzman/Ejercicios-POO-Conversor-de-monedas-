# Intenta crear una clase Dado que cumpla los
# siguientes requerimientos:
# el dado debe tener un número de caras (por defecto 6)
# debe ser capaz de lanzarse y devolver un número aleatorio
# entre 1 y el número de caras.

import random

class Dado():
    def __init__(self,caras=6):
        self.caras = caras
    
    def lanzar(self):
        resultado = random.randint(1,self.caras)
        return resultado
    
dado = Dado()

print(f'Lanzando dado con caras por defecto: {dado.lanzar()}')

dado2 = Dado(20)

print(f'Lanzando dado de 20 caras: {dado2.lanzar()}')
    

