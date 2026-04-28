
def convertir_monedas(eleccion, monedas):
    total_usd = eleccion.convertir_usd()
    print(f'{eleccion}. equivalente en usd: ${total_usd}')