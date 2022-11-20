from lecturacsv import *
from Pedidos import *

numero_referido = int(clientela[i][8])
for i in range(len(clientela)):
    if numero_referido > 0:
        clientela[i][8] = int(clientela[i][8]) - 1
        precio = precio - 0.20
        pass
    else:
        print("No cuenta con puntos de referido")
