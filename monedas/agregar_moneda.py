def agregar_moneda():
    while True:
        nombre = input(" Ingresa el nombre de la moneda: ").lower().strip()
        try:
            cantidad = float(input(" Ingresa la cantidad: "))
            tasa_usd = float(input(" Ingresa la tasa a USD: "))
            return nombre, cantidad, tasa_usd
        except:
            print(" El valor ingresado no corresponde a un numero, intentelo de nuevo.")
