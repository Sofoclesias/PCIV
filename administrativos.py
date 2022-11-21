from lecturacsv import *

def menu_admin():
    while True:
        op0 = int(input('''
        1. Gestionar pedidos
        2. Gestionar existencias
        3. Gestionar cuentas
        4. Salir

        Selecciona tu opción: '''))
        print('\n', '#' * 50)
        if op0 == 1:
            print("Pedidos")

        elif op0 == 2:
            while True:
                op1 = int(input('''
                                1. Pizzas
                                2. Extras
                                3. Salir

                                Selecciona tu opción: '''))
                print('\n', '#' * 50)
                if op1 == 1:
                    op2 = int(input('''
                                                                        1. Visualizar pizzas
                                                                        2. Añadir pizzas
                                                                        3. Eliminar pizzas
                                                                        4. Modificar pizzas
                                                                        5. Salir

                                                                        Selecciona tu opción: '''))

                    if op2 == 1:
                        print("Visualizando todas las pizzas.")
                        zas = sorted(prod, key=lambda x: (x[2], x[3]), reverse=True)
                        print("{0:<5s}{1:<20s}{2:>20s}{3:>20s}".format("ID", "Nombre", "Precio", "Cantidad"))

                        for i in range(len(zas)):
                            print("{0:<5s}{1:<20s}{2:>20s}{3:>20d}".format(str(zas[i][0]), zas[i][1], str(zas[i][2]),
                                                                           zas[i][3]))
                    elif op2 == 2:
                        while True:
                            try:
                                nomx = input("Ingrese nombre de la pizza: ")
                                px = float(input("Ingrese precio de la pizza: "))
                                nx = int(input("Ingresar cantidad de pizzas que ofrecer: "))

                                idx = len(prod) + 1
                                print("\n{0:<20s}{1:>20s}{2:>20s}".format("Nombre", "Precio", "Cantidad"))
                                print("{0:<20s}{1:>20s}{2:>20s}".format(nomx, str(px), str(nx)))

                                ver = input("\n¿Seguro que deseas añadir esta pizza? (y/n): ").lower()
                                if ver == "y":
                                    actualizarcsv(csvpizzas, [idx, nomx, px, nx])
                                    prod.append([idx, nomx, px, nx])
                                    break
                                else:
                                    pass
                            except:
                                print("Ingrese datos válidos.")
                    elif op2 == 3:
                        zasFlag = True
                        ix = None
                        while zasFlag:
                            zasx = input(
                                "Ingrese el ID de la pizza que deseas eliminar (para cancelar,escribir n): ")
                            if zasx == "n":
                                zasFlag = False
                                break
                            if zasx != "n":
                                for i in range(len(prod)):
                                    if zasx == prod[i][0]:
                                        ix = i
                                        zasFlag = False
                                        break

                                if zasFlag:
                                    print("No se ha encontrado la pizza. Inténtelo de nuevo.")
                        if ix != None:
                            print("\n{0:<20s}{1:>20s}{2:>20s}".format("Nombre", "Precio", "Cantidad"))
                            print("{0:<20s}{1:>20s}{2:>20s}".format(prod[ix][1], prod[ix][2], prod[ix][3]))
                            while True:
                                ver = input("¿Seguro que deseas eliminar esta pizza? (y/n): ")
                                if ver == "n":
                                    break
                                elif ver == "y":
                                    eliminarfilacsv(csvpizzas, ix)
                                    prod.pop(ix)
                                    print("Pizza eliminada satisfactoriamente.")
                                    break
                    elif op2 == 4:
                        zasFlag = True
                        ix = None
                        while zasFlag:
                            zasx = input(
                                "Ingrese el ID de la pizza que deseas modificar (para cancelar,escribir n): ")
                            if zasx == "n":
                                zasFlag = False
                                break
                            if zasx != "n":
                                for i in range(len(prod)):
                                    if zasx == prod[i][0]:
                                        ix = i
                                        zasFlag = False
                                        break

                                if zasFlag:
                                    print("No se ha encontrado la pizza. Inténtelo de nuevo.")
                        if ix != None:
                            print("\n{0:<20s}{1:>20s}{2:>20s}".format("Nombre", "Precio", "Cantidad"))
                            print("{0:<20s}{1:>20s}{2:>20s}".format(prod[ix][1], prod[ix][2], prod[ix][3]))
                            while True:
                                op3 = int(input('''¿Qué deseas modificar?
                                                            1. Nombre
                                                            2. Precio
                                                            3. Cantidad
                                                            4. Salir

                                                            Selecciona tu opción: '''))
                                if op3 == 1:
                                    nomx = input("Ingrese nuevo nombre: ")
                                    ver = input("¿Seguro que deseas cambiar el nombre de la pizza? (y/n): ")
                                    if ver == "n":
                                        break
                                    elif ver == "y":
                                        modificarvalorcsv(csvpizzas, nomx, ix, 1)
                                        prod[ix][1] = nomx
                                        print("Pizza actualizada.")
                                        break
                                elif op3 == 2:
                                    px = float(input("Ingrese nuevo precio: "))
                                    ver = input("¿Seguro que deseas cambiar el precio de la pizza? (y/n): ")
                                    if ver == "n":
                                        break
                                    elif ver == "y":
                                        modificarvalorcsv(csvpizzas, px, ix, 2)
                                        prod[ix][2] = px
                                        print("Pizza actualizada.")
                                        break
                                elif op3 == 3:
                                    stockx = input("Ingrese nuevo stock: ")
                                    ver = input("¿Seguro que deseas cambiar la cantidad de la pizza? (y/n): ")
                                    if ver == "n":
                                        break
                                    elif ver == "y":
                                        modificarvalorcsv(csvpizzas, stockx, ix, 3)
                                        prod[ix][3] = stockx
                                        print("Pizza actualizada.")
                                        break
                                elif op3 == 4:
                                    break
                                else:
                                    print("Ingrese una opción válida.")

                    elif op2 == 5:
                        break
                    else:
                        print("Ingrese una opción válida.")
                if op1 == 2:
                    op2 = int(input('''
                                                    1. Visualizar extras
                                                    2. Añadir extras
                                                    3. Eliminar extras
                                                    4. Modificar extras
                                                    5. Salir

                                                    Selecciona tu opción: '''))

                    if op2 == 1:
                        print("Visualizando todos los extras.")
                        ex = sorted(extras, key=lambda x: (x[2], x[3]), reverse=True)
                        print("{0:<5s}{1:<20s}{2:>20s}{3:>20s}".format("ID", "Nombre", "Precio", "Cantidad"))

                        for i in range(len(ex)):
                            print("{0:<5s}{1:<20s}{2:>20s}{3:>20d}".format(str(ex[i][0]), ex[i][1], str(ex[i][2]),
                                                                           ex[i][3]))
                    elif op2 == 2:
                        while True:
                            try:
                                nomx = input("Ingrese nombre del extra: ")
                                px = float(input("Ingrese precio del extra: "))
                                nx = int(input("Ingresar cantidad de extra que ofrecer: "))

                                idx = len(extras) + 1
                                print("\n{0:<20s}{1:>20s}{2:>20s}".format("Nombre", "Precio", "Cantidad"))
                                print("{0:<20s}{1:>20s}{2:>20s}".format(nomx, str(px), str(nx)))

                                ver = input("\n¿Seguro que deseas añadir este extra? (y/n): ").lower()
                                if ver == "y":
                                    actualizarcsv(csvextras, [idx, nomx, px, nx])
                                    extras.append([idx, nomx, px, nx])
                                    break
                                else:
                                    pass
                            except:
                                print("Ingrese datos válidos.")
                    elif op2 == 3:
                        exFlag = True
                        ix = None
                        while exFlag:
                            exx = input(
                                "Ingrese el ID del extra que deseas eliminar (para cancelar,escribir n): ")
                            if exx == "n":
                                exFlag = False
                                break
                            if exx != "n":
                                for i in range(len(extras)):
                                    if exx == extras[i][0]:
                                        ix = i
                                        exFlag = False
                                        break

                                if exFlag:
                                    print("No se ha encontrado al extra. Inténtelo de nuevo.")
                        if ix != None:
                            print("\n{0:<20s}{1:>20s}{2:>20s}".format("Nombre", "Precio", "Cantidad"))
                            print("{0:<20s}{1:>20s}{2:>20s}".format(extras[ix][1], extras[ix][2], extras[ix][3]))
                            while True:
                                ver = input("¿Seguro que deseas eliminar este extra? (y/n): ")
                                if ver == "n":
                                    break
                                elif ver == "y":
                                    eliminarfilacsv(csvextras, ix)
                                    extras.pop(ix)
                                    print("Extra elimimnado satisfactoriamente.")
                                    break
                    elif op2 == 4:
                        exFlag = True
                        ix = None
                        while exFlag:
                            exx = input(
                                "Ingrese el ID de la extra que deseas modificar (para cancelar,escribir n): ")
                            if exx == "n":
                                exFlag = False
                                break
                            if exx != "n":
                                for i in range(len(extras)):
                                    if exx == extras[i][0]:
                                        ix = i
                                        exFlag = False
                                        break

                                if exFlag:
                                    print("No se ha encontrado el extra. Inténtelo de nuevo.")
                        if ix != None:
                            print("\n{0:<20s}{1:>20s}{2:>20s}".format("Nombre", "Precio", "Cantidad"))
                            print("{0:<20s}{1:>20s}{2:>20s}".format(extras[ix][1], extras[ix][2], extras[ix][3]))
                            while True:
                                op3 = int(input('''¿Qué deseas modificar?
                                        1. Nombre
                                        2. Precio
                                        3. Cantidad
                                        4. Salir

                                        Selecciona tu opción: '''))
                                if op3 == 1:
                                    nomx = input("Ingrese nuevo nombre: ")
                                    ver = input("¿Seguro que deseas cambiar el nombre del extra? (y/n): ")
                                    if ver == "n":
                                        break
                                    elif ver == "y":
                                        modificarvalorcsv(csvextras, nomx, ix, 1)
                                        extras[ix][1] = nomx
                                        print("Extra actualizado.")
                                        break
                                elif op3 == 2:
                                    px = float(input("Ingrese nuevo precio: "))
                                    ver = input("¿Seguro que deseas cambiar el precio del extra? (y/n): ")
                                    if ver == "n":
                                        break
                                    elif ver == "y":
                                        modificarvalorcsv(csvextras, px, ix, 2)
                                        extras[ix][2] = px
                                        print("Extra actualizado.")
                                        break
                                elif op3 == 3:
                                    stockx = input("Ingrese nuevo stock: ")
                                    ver = input("¿Seguro que deseas cambiar el cantidad del extra? (y/n): ")
                                    if ver == "n":
                                        break
                                    elif ver == "y":
                                        modificarvalorcsv(csvextras, stockx, ix, 3)
                                        extras[ix][3] = stockx
                                        print("Extra actualizado.")
                                        break
                                elif op3 == 4:
                                    break
                                else:
                                    print("Ingrese una opción válida.")

                    elif op2 == 5:
                        break
                    else:
                        print("Ingrese una opción válida.")
                if op1 == 3:
                    break

        elif op0 == 3:
            while True:
                op1 = int(input('''
                1. Visualizar clientes
                2. Eliminar clientes
                3. Salir

                Selecciona tu opción: '''))
                print('\n', '#' * 50)

                if op1 == 1:
                    while True:
                        op2 = int(input('''
                                        1. Visualizar todo
                                        2. Filtrar por clientes con pedidos
                                        3. Filtrar por clientes con puntos
                                        4. Salir

                                        Selecciona tu opción: '''))
                        print('\n', '#' * 50)
                        if op2 == 1:
                            print("Visualizando todos los clientes")
                            print(
                                "{0:<20s}{1:<20s}{2:<20s}{3:<20s}{4:>20s}{5:>20s}".format("DNI", "Nombres", "Apellidos",
                                                                                          "Usuario",
                                                                                          "Número de pedidos",
                                                                                          "Puntos de referidos"))

                            for i in range(len(clientela)):
                                if isinstance(clientela[i][7], list):
                                    x = len(clientela[i][7])
                                else:
                                    x = str(0)

                                print("{0:<20s}{1:<20s}{2:<20s}{3:<20s}{4:>20s}{5:>20s}".format(clientela[i][0],
                                                                                                clientela[i][1],
                                                                                                clientela[i][2],
                                                                                                clientela[i][4], x,
                                                                                                clientela[i][8]))
                        elif op2 == 2:
                            print("Visualizando clientes con pedidos")
                            print(
                                "{0:<20s}{1:<20s}{2:<20s}{3:<20s}{4:>20s}{5:>20s}".format("DNI", "Nombres", "Apellidos",
                                                                                          "Usuario",
                                                                                          "Número de pedidos",
                                                                                          "Puntos de referidos"))

                            for i in range(len(clientela)):
                                if isinstance(clientela[i][7], list):
                                    print("{0:<20s}{1:<20s}{2:<20s}{3:<20s}{4:>20s}{5:>20s}".format(clientela[i][0],
                                                                                                    clientela[i][1],
                                                                                                    clientela[i][2],
                                                                                                    clientela[i][4],
                                                                                                    str(len(
                                                                                                        clientela[i][
                                                                                                            7])),
                                                                                                    clientela[i][8]))
                                else:
                                    continue


                        elif op2 == 3:
                            print("Visualizando clientes con puntos")
                            print(
                                "{0:<20s}{1:<20s}{2:<20s}{3:<20s}{4:>20s}{5:>20s}".format("DNI", "Nombres", "Apellidos",
                                                                                          "Usuario",
                                                                                          "Número de pedidos",
                                                                                          "Puntos de referidos"))

                            for i in range(len(clientela)):
                                if int(clientela[i][8]) > 0:
                                    if isinstance(clientela[i][7], list):
                                        x = len(clientela[i][7])
                                    else:
                                        x = str(0)

                                    print(
                                        "{0:<20s}{1:<20s}{2:<20s}{3:<20s}{4:>20s}{5:>20s}".format(clientela[i][0],
                                                                                                  clientela[i][1],
                                                                                                  clientela[i][4],
                                                                                                  clientela[i][2],
                                                                                                  x, clientela[i][8]))
                                else:
                                    continue
                        elif op2 == 4:
                            break
                        else:
                            print(' Ingresa una opcion del menú')
                elif op1 == 2:
                    usuFlag = True
                    ix = None
                    while usuFlag:
                        usux = input("Ingrese el nombre del usuario que deseas eliminar (para cancelar,escribir n): ")
                        if usux == "n":
                            usuFlag = False
                            break
                        if usux != "n":
                            for i in range(len(clientela)):
                                if usux == clientela[i][4]:
                                    ix = i
                                    usuFlag = False
                                    break

                            if usuFlag:
                                print("No se ha encontrado al usuario. Inténtelo de nuevo.")
                    if ix != None:
                        print("{0:<20s}{1:<20s}{2:<20s}{3:<20s}{4:>20s}{5:>20s}".format("DNI", "Nombres",
                                                                                        "Apellidos", "Usuario",
                                                                                        "Número de pedidos",
                                                                                        "Puntos de referidos"))
                        print("{0:<20s}{1:<20s}{2:<20s}{3:<20s}{4:>20s}{5:>20s}".format(clientela[ix][0],
                                                                                        clientela[ix][1],
                                                                                        clientela[ix][2],
                                                                                        clientela[ix][4],
                                                                                        str(len(clientela[ix][7])),
                                                                                        clientela[ix][8]))
                        while True:
                            ver = input("¿Seguro que deseas eliminar este usuario? (y/n): ")
                            if ver == "n":
                                break
                            elif ver == "y":
                                eliminarfilacsv(csvclientes, ix)
                                clientela.pop(ix)
                                print("Usuario elimimnado satisfactoriamente.")
                                break


                elif op1 == 3:
                    break
        elif op0 == 4:
            break
        else:
            print(' Ingresa una opcion del menú')


menu_admin()
