from entidades.cliente import Cliente
from enums.tarifa import Tarifa
from datetime import datetime

class Recibo:
    def __init__(self, consumo: int, cliente: Cliente, fecha: datetime):
        self.consumo = consumo
        self.cliente = cliente
        self.fecha = fecha
    
    def calcular_precio_pagar (self) -> float:
        if self.consumo <= 1000:
            return self.consumo * Tarifa.TARIFA_PERSONA_FISICA.value
        elif self.consumo >= 50000:
            return self.consumo * Tarifa.TARIFA_EMPRESARIAL.value