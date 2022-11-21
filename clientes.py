import clases as cl
import lecturacsv as lec
import Pedidos as ped

def menu_clientes(usux, contx):
    for i in range(len(lec.clientela)):
        if usux == lec.clientela[i][4] and contx == lec.clientela[i][5]:
            yo = lec.clientela[i]
            ix = i
            cliente_creacion = cl.Cliente(lec.clientela[i][0], lec.clientela[i][1], lec.clientela[i][2],
                                          lec.clientela[i][3], lec.clientela[i][4], lec.clientela[i][5],
                                          lec.clientela[i][6], lec.clientela[i][7], lec.clientela[i][8])
    while True:
        while True:
            try:
                opcion = int(input("¿que desea realizar?\n"
                                   "1.actuaizar datos\n"
                                   "2.realizar un pedido\n"
                                   "3.salir\n"
                                   "\n"
                                   "escriba una opción: "))
                if str(opcion) in "123":
                    break
                else:
                    print("escriba una opción correcta\n")
                    pass
            except:
                print("escriba una opción correcta\n")
                pass
        if opcion == 3:
            break
        if opcion == 1:
            while True:
                print("{0:<10} {1:>20} {2:>20} {3:>20}".format("DNI", "NOMBRE", "APELLIDO", "EDAD"))
                print("{0:<20} {1:>20} {2:>20} {3:>20}".format(yo[0], yo[1], yo[2], yo[3]))

                while True:
                    try:
                        rpta = int(input("¿que desea hacer?\n"
                                         "1.cambiar metodo de pago\n"
                                         "2.cambiar DNI\n"
                                         "3.cambiar nombre\n"
                                         "4.cambiar apellidos\n"
                                         "5.cambiar edad\n"
                                         "6.salir\n"
                                         "ingrese una opción: "))
                        break
                    except:
                        print("Ingrese una opción válida: ")

                if rpta == 6:
                    break
                if rpta == 1:
                    lec.modificarvalorcsv(lec.csvclientes, lec.refPago(), ix, 6)
                if rpta == 2:
                    while True:
                        try:
                            nuevo_dni = input("ingrese el nuevo dni")
                            if len(nuevo_dni) == 8 and int(nuevo_dni) > 0:
                                break
                            else:
                                print("escriba un dni válido")
                        except:
                            print("escriba un dni válido")
                    lec.modificarvalorcsv(lec.csvclientes, nuevo_dni, ix, 0)
                if rpta == 3:
                    while True:
                        try:
                            nuevo_nombre = input("ingrese el nuevo nombre: ")
                            if len(nuevo_nombre) != nuevo_nombre.count(" "):
                                break
                            else:
                                print("escriba un nombre válido")
                        except:
                            print("escriba un nombre válido")
                    lec.modificarvalorcsv(lec.csvclientes, nuevo_nombre, ix, 1)

                if rpta == 4:
                    while True:
                        try:
                            nuevo_apellido = input("ingrese el nuevo apellido: ")
                            if len(nuevo_apellido) != nuevo_apellido.count(" "):
                                break
                            else:
                                print("escriba un apellido válido")
                        except:
                            print("escriba un nombre válido")
                    lec.modificarvalorcsv(lec.csvclientes, nuevo_apellido, ix, 2)

                if rpta == 5:
                    while True:
                        try:
                            nuevo_edad = int(input("ingrese la nueva edad: "))
                            if nuevo_edad >= 18:
                                break
                            else:
                                print("escriba una edad válida")
                        except:
                            print("escriba una edad válida")
                    lec.modificarvalorcsv(lec.csvclientes, nuevo_edad, ix, 1)

        if opcion == 2:
            listpedidos = ped.realizarpedidos(yo, ix)
            ped.realizar_pago(listpedidos, yo, ix)
