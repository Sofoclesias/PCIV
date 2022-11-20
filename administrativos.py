def menu_admin(clientela):
    while True:
        op0 = int(input('''
        1. Gestionar existencias
        2. Gestionar pedidos
        3. Gestionar clientes
        4. Salir

        Selecciona tu opción: '''))
        print('\n', '#' * 50)
        if op0 == 1:
            print("Existencias")
        elif op0 == 2:
            print("Pedidos")
        elif op0 == 3:
            while True:
                op1 = int(input('''
                1. Visualizar todos
                2. Filtrar por clientes con pedidos
                3. Filtrar por clientes con puntos
                4. Salir

                Selecciona tu opción: '''))
                print('\n', '#' * 50)
                if op1 == 1:
                    print("Visualizando todos los clientes")
                    print("{0:<20s}{1:>20s}{2:>20s}{3:>20s}{4:>20s}".format("DNI", "Nombres", "Apellidos",
                                                                            "Número de pedidos", "Puntos de referidos"))

                    for i in range(len(clientela)):
                        if isinstance(clientela[i][7], list):
                            x = len(clientela[i][7])
                        else:
                            x = 0

                        print("{0:<20s}{1:>20s}{2:>20s}{3:>20s}{4:>20s}".format(clientela[i][0], clientela[i][1],
                                                                                clientela[i][2], x, clientela[i][8]))
                elif op1 == 2:
                    print("Visualizando clientes con pedidos")
                    print("{0:<20s}{1:>20s}{2:>20s}{3:>20s}{4:>20s}".format("DNI", "Nombres", "Apellidos",
                                                                            "Número de pedidos", "Puntos de referidos"))

                    for i in range(len(clientela)):
                        if isinstance(clientela[i][7], list):
                            print("{0:<20s}{1:>20s}{2:>20s}{3:>20s}{4:>20s}".format(clientela[i][0], clientela[i][1],
                                                                                    clientela[i][2],
                                                                                    len(clientela[i][7]),
                                                                                    clientela[i][8]))
                        else:
                            continue


                elif op1 == 3:
                    print("Visualizando clientes con puntos")
                    print("{0:<20s}{1:>20s}{2:>20s}{3:>20s}{4:>20s}".format("DNI", "Nombres", "Apellidos",
                                                                            "Número de pedidos", "Puntos de referidos"))

                    for i in range(len(clientela)):
                        if int(clientela[i][8]) > 0:
                            if isinstance(clientela[i][7], list):
                                x = len(clientela[i][7])
                            else:
                                x = 0

                            print(
                                "{0:<20s}{1:>20s}{2:>20s}{3:>20s}{4:>20s}".format(clientela[i][0], clientela[i][1],
                                                                                  clientela[i][2],
                                                                                  x, clientela[i][8]))
                        else:
                            continue
                elif op1 == 4:
                    break
                else:
                    print(' Ingresa una opcion del menú')
        elif op0 == 4:
            break
        else:
            print(' Ingresa una opcion del menú')
