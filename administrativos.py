from lecturacsv import *

print(clientela)


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
                    print("Pizzas")
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
                        print("{0:<20s}{1:>20s}{2:>20s}".format("Nombre", "Precio", "Cantidad"))

                        for i in range(len(ex)):
                            print("{0:<20s}{1:>20s}{2:>20d}".format(ex[i][1], str(ex[i][2]), ex[i][3]))
                    elif op2 == 2:
                        while True:
                            try:
                                nomx = input("Ingrese nombre de la pizza: ")
                                px = float(input("Ingrese precio de la pizza: "))
                                nx = int(input("Ingresar cantidad de pizzas que ofrecer: "))

                                print("\n{0:<20s}{1:>20s}{2:>20s}".format("Nombre", "Precio", "Cantidad"))
                                print("{0:<20s}{1:>20s}{2:>20s}".format(nomx, str(px), str(nx)))

                                ver = input("\n¿Seguro que deseas añadir esta pizza? (y/n): ").lower()
                                if ver == "y":
                                    actualizarcsv(csvextras, [nomx, px, nx])
                                    break
                                else:
                                    pass
                            except:
                                print("Ingrese datos válidos.")
                    elif op2 == 3:
                        print("eliminar")
                    elif op2 == 4:
                        print("tu vieja")
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
