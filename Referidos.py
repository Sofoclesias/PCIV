from lecturacsv import *
from Pedidos import *

for i in range(len(clientela)):
    numero_referido = int(clientela[i][8])
    print("Puntos de referido: ", numero_referido)
    if numero_referido > 0:
        clientela[i][8] = int(clientela[i][8]) - 1
        precio = precio - 0.50
        pass
    else:
        print("No cuenta con puntos de referido")

