from entidades.cliente import Cliente
from entidades.recibo import Recibo
from datetime import datetime

cliente1 = Cliente("Carlos Rodríguez", "Calle 8 y 9 av 3 colonia Marsella", 6221475454)

recibo = Recibo(10000, cliente1, datetime.now ())


print("Recibo emitido por la CFE")
print(f"Fecha de emisión {recibo.fecha}")
print(f"Cliente: {recibo.cliente.nombre}")
print(f"Dirección: {recibo.cliente.dirección}")
print(f"Watts consumidos: {recibo.consumo}")
print(f"Precio a pagar: {recibo.calcular_precio_pagar()}")