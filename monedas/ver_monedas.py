def ver_monedas(monedas):
    print('Estas son tus monedas por el momendo: ')

    for numero, moneda in enumerate(monedas, start=1):
        print(f'{numero} - {moneda}')