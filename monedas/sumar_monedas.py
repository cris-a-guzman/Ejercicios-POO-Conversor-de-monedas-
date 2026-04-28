
def sumar_monedas(*monedas):
    if not monedas:
        return None
    print(' Elegiste las monedas: ')
    for i in monedas:
        print(" - ", i)
    total = monedas[0]

    for moneda in monedas[1:]:
        total += moneda
    print(total)
        