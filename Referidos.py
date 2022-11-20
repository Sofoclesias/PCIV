import lecturacsv as lec
import Pedidos as ped

numero_referido = lec.clientela[i][8]
if numero_referido > 0:
    ped.precio = ped.precio - 0.20

else:
    print("No cuenta con puntos de referido")
