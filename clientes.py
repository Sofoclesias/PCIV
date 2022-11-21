# import clases as cl
from lecturacsv import *
from random import *
import copy


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
    carritoprod, carritoext = [], []
    precioprod, precioext = [], []

    muestraprod = copy.deepcopy(prod)
    muestraextra = copy.deepcopy(extras)
    while True:
        try:
            print("Menú Productos".center(31, "*"))
            print("{0:<4}{3}{1:<19}{3}{2:^6}{4:^8}".format("ID", "Productos", "Precios", "|", "stock"))

            for i in muestraprod:
                print("{0:<4}{3}{1:<19}{3}{2:>6}{4:^10}".format(i[0], i[1], i[2], "|", i[3]))
            print("Si desea salir, ingrese 0.\n")
            opcprod = int(input("¿Qué producto desea ordenar?: "))
            print("\n")
            if 0 < opcprod:
                inShop = True
                for i in range(len(muestraprod)):
                    if int(opcprod) == muestraprod[i][0]:
                        ix = i
                        inShop = False
                        break

                if inShop:
                    print("Ingrese un ID válido.")
                else:
                    if muestraprod[ix][3] == 0:
                        print("No hay unidades disponibles.")
                    else:
                        print("¿Cuántas unidades?")
                        while True:
                            try:
                                cantidad = int(input("Ingrese la cantidad de pizzas: "))
                                if 0 < cantidad <= muestraprod[ix][3]:
                                    break
                            except:
                                print("Ingrese una cantidad válida.")
                        muestraprod[ix][3] -= cantidad

                        inCar = True
                        for j in range(len(carritoprod)):
                            if carritoprod[j][0] == muestraprod[ix][1]:
                                carritoprod[j][1] = int(carritoprod[j][1]) + cantidad
                                precioprod[j] = int(precioprod[j]) + round(int(muestraprod[ix][2]) * cantidad, 1)
                                inCar = False

                        if inCar:
                            carritoprod.append(
                                [muestraprod[ix][1], "{}".format(cantidad), "{}".format(muestraprod[ix][2])])
                            precioprod.append(round(muestraprod[ix][2] * cantidad, 1))
            elif opcprod == 0:
                break
            else:
                print("Ingrese una opción válida\n")
        except:
            print("Ingrese una opcion válida\n")

    while True:
        try:
            print("Menú Extras".center(31, "*"))
            print("{0:4}{3}{1:<19}{3}{2:^6}{4:^8}".format("ID", "Productos", "Precios", "|", "stock"))
            for i in muestraextra:
                print("{0:<4}{3}{1:<19}{3}{2:>6}{4:^8}".format(i[0], i[1], i[2], "|", i[3]))
            print("Si desea salir, ingrese 0\n")
            opcext = int(input("¿Qué extras desea añadir? "))
            print("\n")
            if 0 < opcext:
                inShop = True
                for i in range(len(muestraextra)):
                    if int(opcext) == muestraextra[i][0]:
                        ix = i
                        inShop = False
                        break

                if inShop:
                    print("Ingrese un ID válido.")
                else:
                    if muestraextra[ix][3] == 0:
                        print("No hay unidades disponibles.")
                    else:
                        print("¿Cuántas unidades?")
                        while True:
                            try:
                                cantidad = int(input("Ingrese la cantidad de extras: "))
                                if 0 < cantidad <= muestraextra[ix][3]:
                                    break
                            except:
                                print("Ingrese una cantidad válida.")
                        muestraextra[ix][3] -= cantidad

                        inCar = True
                        for j in range(len(carritoext)):
                            if carritoext[j][0] == muestraextra[ix][1]:
                                carritoext[j][1] = int(carritoext[j][1]) + cantidad
                                precioext[j] = int(precioext[j]) + round(int(muestraextra[ix][2]) * cantidad, 1)
                                inCar = False

                        if inCar:
                            carritoext.append(
                                [muestraextra[ix][1], "{}".format(cantidad), "{}".format(muestraextra[ix][2])])
                            precioext.append(round(muestraextra[ix][2] * cantidad, 1))
            elif opcext == 0:
                break
            else:
                print("Ingrese una opción válida\n")
        except:
            print("Ingrese una opción válida.")

    ran = str(randint(1, 99999999))
    if len(ran) < 8:
        ran = ran.zfill(8)
    codigo = "P" + ran
    pedido_global = [codigo, carritoprod, carritoext]

    if len(carritoprod) == 0 and len(carritoext) == 0:
        return pedido_global
    else:
        print("Precio total:", sum(precioext) + sum(precioprod))

        px = sum(precioext) + sum(precioprod)

        if int(yo[8]) > 0:
            yo[8] = int(yo[8]) - 1
            px -= 0.5
            modificarvalorcsv(csvclientes, yo[8], ix, 8)
            print("El nuevo precio tras el descuento de referidos es: ", px)

        global pedcsvx

        pedcsvx = [codigo, yo[4], transcribir(carritoprod), transcribir(carritoext), px]

        return pedido_global


def realizar_pago(listpedidos, yo, ix):
    while True:
        if len(listpedidos[1]) == 0 and len(listpedidos[2]) == 0:
            print("No ha realizado ningún pedido.\n")
            break
        else:
            print("{0:50}".format("Su pedido es:"))
            lista_pedido(listpedidos)

            if yo[6] == "None" or yo[6] == None:
                print("Usted no tiene una tarjeta de pago.")
                meth = refPago()
                if meth == None:
                    break
                else:
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

                    actualizarcsv(csvpedidos, pedcsvx)
                    print("Pago realizado con éxito.")
                    break
                elif ver == "n":
                    break


def menu_clientes(usux, contx):
    try:
        for i in range(len(clientela)):
            if usux == clientela[i][4] and contx == clientela[i][5]:
                yo = clientela[i]
                ix = i
                cliente_creacion = cl.Cliente(clientela[i][0], clientela[i][1], clientela[i][2],
                                              clientela[i][3], clientela[i][4], clientela[i][5],
                                              clientela[i][6], clientela[i][7], clientela[i][8])
        while True:
            while True:

                opcion = int(input("¿Qué desea realizar?: \n"
                                   "1. Actualizar datos\n"
                                   "2. Realizar un pedido\n"
                                   "3. Salir\n"
                                   "\n"
                                   "Selecciona una opción: "))
                if opcion == 3:
                    break
                elif opcion == 1:
                    while True:
                        print("{0:<20} {1:>20} {2:>20} {3:>20}".format("DNI", "NOMBRE", "APELLIDO", "EDAD"))
                        print("{0:<20} {1:>20} {2:>20} {3:>20}".format(yo[0], yo[1], yo[2], yo[3]))

                        try:
                            rpta = int(input("\n¿Qué desea hacer?:\n\n"
                                             "1. Cambiar método de pago\n"
                                             "2. Cambiar DNI\n"
                                             "3. Cambiar nombre\n"
                                             "4. Cambiar apellidos\n"
                                             "5. Cambiar edad\n"
                                             "6. Salir\n"
                                             "ingrese una opción: "))
                        except:
                            print("Ingrese una opción válida. ")

                        if rpta == 6:
                            break
                        elif rpta == 1:
                            modificarvalorcsv(csvclientes, refPago(), ix, 6)
                        elif rpta == 2:
                            while True:
                                try:
                                    nuevo_dni = input("Ingrese el nuevo DNI: ")
                                    if len(nuevo_dni) == 8 and int(nuevo_dni) > 0:
                                        modificarvalorcsv(csvclientes, nuevo_dni, ix, 0)
                                        yo[0], clientela[ix][0] = nuevo_dni, nuevo_dni
                                        break
                                    else:
                                        print("Escriba un DNI válido.")
                                except:
                                    print("Escriba un DNI válido.")

                        elif rpta == 3:
                            while True:
                                try:
                                    nuevo_nombre = input("Ingrese el nuevo nombre: ")
                                    if len(nuevo_nombre) != nuevo_nombre.count(" ") and tiene_numeros(
                                            nuevo_nombre) == False:
                                        modificarvalorcsv(csvclientes, nuevo_nombre, ix, 1)
                                        yo[1], clientela[ix][1] = nuevo_nombre, nuevo_nombre
                                        break
                                    else:
                                        print("Escriba un nombre válido.")
                                except:
                                    print("Escriba un nombre válido.")

                        elif rpta == 4:
                            while True:
                                try:
                                    nuevo_apellido = input("Ingrese el nuevo apellido: ")
                                    if len(nuevo_apellido) != nuevo_apellido.count(" ") and tiene_numeros(
                                            nuevo_apellido) == False:
                                        modificarvalorcsv(csvclientes, nuevo_apellido, ix, 2)
                                        yo[2], clientela[ix][2] = nuevo_apellido, nuevo_apellido
                                        break
                                    else:
                                        print("Escriba un apellido válido.")
                                except:
                                    print("Escriba un nombre válido.")


                        elif rpta == 5:
                            while True:
                                try:
                                    nuevo_edad = int(input("Ingrese la nueva edad: "))
                                    if nuevo_edad >= 18:
                                        modificarvalorcsv(csvclientes, nuevo_edad, ix, 3)
                                        yo[3], clientela[ix][3] = nuevo_edad, nuevo_edad
                                        break
                                    else:
                                        print("Escriba una edad válida.")
                                except:
                                    print("Escriba una edad válida.")

                        else:
                            print("Ingrese una opción válida: ")

                elif opcion == 2:
                    listpedidos = realizarpedidos(yo, ix)
                    realizar_pago(listpedidos, yo, ix)

                elif opcion == 3:
                    break

                else:
                    print("Escriba una opción válida.\n")
    except:
        print("Escriba una opción válida.\n")
