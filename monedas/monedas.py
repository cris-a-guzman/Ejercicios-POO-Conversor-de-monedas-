class Moneda:

    def __init__(self, nombre, cantidad, tasa_usd=1.0):
        self.nombre = nombre
        self.cantidad = cantidad
        self.tasa_usd = tasa_usd

    def convertir_usd(self):
        
        return self.cantidad * self.tasa_usd

    def __add__(self, other):
        total_usd = self.convertir_usd() + other.convertir_usd()
        return Moneda("USD", round(total_usd,2), 1)
    
    def __str__(self) -> str:
        return f"{self.nombre}: {self.cantidad:.2f}"