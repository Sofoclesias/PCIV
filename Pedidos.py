from random import *
from lecturacsv import *


carritoprod = []
carritoext = []
precio = []


def realizarpedidos(usux, contx):
    while True:
        while True:
            try:
                print("Menú Productos".center(31, "*"))
                print("{0:<4}{3}{1:<19}{3}{2:^6}{4:^8}".format("ID", "Productos", "Precios", "|", "stock"))
                for i in prod:
                    print("{0:<4}{3}{1:<19}{3}{2:>6}{4:^10}".format(i[0], i[1], i[2], "|", i[3]))
                print("Si desea salir, ingrese 0\n")
                opcprod = int(input("¿Qué producto desea ordenar? "))
                print("\n")
                if 0 <= opcprod <= len(prod):
                    if opcprod > 0:
                        print("¿Cuántas unidades?")
                        while True:
                            try:
                                cantidad = int(input("Ingrese la cantidad de pizzas: "))
                                for i in prod:
                                    if int(opcprod) == i[0]:
                                        maximo = i[3]
                                if 0 < cantidad <= maximo:
                                    break
                            except:
                                print("Ingrese una cantidad válida")
                        for i in prod:
                            if int(opcprod) == i[0]:
                                carritoprod.append([i[1], "{} unidades".format(cantidad), "precio: {}".format(i[2])])
                                precio.append(round(i[2] * cantidad, 1))
                    break
                else:
                    print("Ingrese una opción válida\n")
            except:
                print("Ingrese una opcion válida\n")
        if opcprod == 0:
            break

    while True:
        while True:
            try:
                print("Menú Extras".center(31, "*"))
                print("{0:4}{3}{1:<19}{3}{2:^6}{4:^8}".format("ID", "Productos", "Precios", "|", "stock"))
                for i in extras:
                    print("{0:<4}{3}{1:<19}{3}{2:>6}{4:^8}".format(i[0], i[1], i[2], "|", i[3]))
                print("Si desea salir, ingrese 0\n")
                opcext = int(input("¿Qué extras desea añadir? "))
                print("\n")
                if 0 <= opcext <= len(extras):
                    if opcext > 0:
                        try:
                            gramos = int(input("Ingrese las unidades extras: "))
                            for i in extras:
                                if int(opcext) == i[0]:
                                    maximo = i[3]
                            if 0 < gramos <= maximo:
                                break
                            else:
                                print("no hay stock suficiente")
                        except:
                            print("esciba una opción valida")
                            pass

                        for i in extras:
                            if int(opcext) == i[0]:
                                carritoext.append([i[1], "{} unidades".format(gramos), "precio: {}".format(i[2])])
                                precio.append(round(i[2] * gramos, 1))
                    break
                else:
                    print("Ingrese una opción válida\n")
            except:
                print("Ingrese una opcion válida\n")
        if opcext == 0:
            break
    ran = str(randint(1, 99999999))
    if len(ran) < 8:
        ran = ran.zfill(8)
    codigo = "P" + ran
    print("el código del pedido es {}".format(codigo).center(80, " "))

    print("Pizzas: ".center(80, "*"))
    for x in carritoprod:
        print("{0:<25}{1:^25}{2:^25}".format(x[0], x[1], x[2]))
    if len(carritoext) > 0:
        print(" Extras: ".center(80, "*"))
        for x in carritoext:
            print("{0:<25}{1:^25}{2:^25}".format(x[0], x[1], x[2]))
    print(" Precio total:", sum(precio))

    px = sum(precio)
    for i in range(len(clientela)):
        if usux == clientela[i][4] and contx == clientela[i][5]:
            print("hola")
            numero_referido = int(clientela[i][8])
            print("Puntos de referido: ", numero_referido)

            if numero_referido > 0:
                clientela[i][8] = int(clientela[i][8]) - 1
                px = px - 0.50
            else:
                pass

    print("El nuevo precio tras el descuento de referidos es: ", px)

    pedido_global = [codigo, carritoprod, carritoext]
    return pedido_global
