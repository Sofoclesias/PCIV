from random import *
from lecturacsv import *

def transcribir(lista):
    if len(lista) == 1:
        constxt = ""
        for i in range(len(lista[0]) - 1):
            constxt += str(lista[0][i]) + "-"
        constxt += str(lista[0][len(lista[0]) - 1])
    else:
        constxt = ""
        for i in range(len(lista)):
            txt = ""
            for j in range(len(lista[0]) - 1):
                txt += str(lista[i][j]) + "-"
            txt += str(lista[i][len(lista[0]) - 1])
            constxt += txt + "|"
        constxt = constxt[:-1]
    return constxt


def lista_pedido(pedido_global):
    print("el código del pedido es {}".format(pedido_global[0]).center(80, " "))

    print("Pizzas: ".center(80, "*"))
    for x in pedido_global[1]:
        print("{0:<25}{1:^25}{2:^25}".format(x[0], x[1], x[2]))
    if len(pedido_global[2]) > 0:
        print(" Extras: ".center(80, "*"))
        for x in pedido_global[2]:
            print("{0:<25}{1:^25}{2:^25}".format(x[0], x[1], x[2]))


def realizarpedidos(yo, ix):
    carritoprod = []
    carritoext = []
    precio = []
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
                                carritoprod.append([i[1], "{}".format(cantidad), "{}".format(i[2])])
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
                        print("¿Cuántas unidades?")
                        while True:
                            try:
                                cantidad = int(input("Ingrese la cantidad de pizzas: "))
                                for i in extras:
                                    if int(opcext) == i[0]:
                                        maximo = i[3]
                                if 0 < cantidad <= maximo:
                                    break
                            except:
                                print("Ingrese una cantidad válida")
                        for i in extras:
                            if int(opcext) == i[0]:
                                carritoext.append([i[1], "{}".format(cantidad), "{}".format(i[2])])
                                precio.append(round(i[2] * cantidad, 1))
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
    pedido_global = [codigo, carritoprod, carritoext]
    print("Precio total:", sum(precio))

    px = sum(precio)

    if int(yo[8]) > 0:
        yo[8] = int(yo[8]) - 1
        px -= 0.5
        modificarvalorcsv(csvclientes, yo[8], ix, 8)
        print("El nuevo precio tras el descuento de referidos es: ", px)

    pedcsvx = [codigo, yo[4], transcribir(carritoprod), transcribir(carritoext), px]
    actualizarcsv(csvpedidos, pedcsvx)
    return pedido_global


def realizar_pago(listpedidos, yo, ix):
    while True:
        print("{0:50}".format("su pedido es:"))
        lista_pedido(listpedidos)

        if yo[6] == "None" == None:
            print("usted no tiene una tarjeta de pago")
            meth = refPago()
            clientela[ix][6] = meth
            modificarvalorcsv(csvclientes, yo[6], ix, 6)
        else:

            ver = input("¿Desea confirmar la compra? (y/n): ").lower()
            if ver == "y":
                for i in range(len(listpedidos[1])):
                    for j in range(len(prod)):
                        if listpedidos[1][i][0] == prod[j][1]:
                            jx = j

                    modificarvalorcsv(csvpizzas, int(prod[jx][3]) - int(listpedidos[1][i][1]), jx, 3)
                    prod[jx][3] = int(prod[jx][3]) - int(listpedidos[1][i][1])

                for i in range(len(listpedidos[2])):
                    for j in range(len(prod)):
                        if listpedidos[2][i][0] == extras[j][1]:
                            jx = j

                    modificarvalorcsv(csvextras, int(extras[jx][3]) - int(listpedidos[2][i][1]), jx, 3)
                    extras[jx][3] = int(extras[jx][3]) - int(listpedidos[2][i][1])

                modificarvalorcsv(csvclientes, int(yo[7]) + 1, ix, 7)
                clientela[ix][7] = int(yo[7]) + 1
                print("Pago realizado con éxito.")
                break
            elif ver == "n":
                break
