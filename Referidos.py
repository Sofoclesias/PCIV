from lecturacsv import *
from Pedidos import *

for i in clientela:
    numero_referido = clientela[i][8]
    if numero_referido > 0:
        precio = precio - 0.20
        pass
    else:
        print("No cuenta con puntos de referido")
