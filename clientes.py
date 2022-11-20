import clases as cl
import lecturacsv as lec


def menu_clientes():
    while True:
        while True:
            try:

                opcion = int(input("¿que desea realizar?\n"
                                   "1.actuaizar datos\n"
                                   "2.realizar un pedido\n"
                                   "3.salir\n"))
                if str(opcion) in "123":
                    break
                else:
                    print("escriba una opción correcta\n")
            except:
                print("escriba una opción correcta\n")

                pass
        if opcion == 3:
            break
        if opcion == 1:
            while True:
                while True:
                    try:

                        rpta = int(input("¿que desea hacer?\n"
                                         "1.cambiar metodo de pago\n"
                                         "2.cambiar DNI\n"
                                         "3.cambiar apellidos\n"
                                         "4.cambiar edad\n"
                                         "5.salir\n"))
                        if str(opcion) in "12345":
                            break
                        else:
                            print("escriba una opción correcta\n")
                    except:
                        print("escriba una opción correcta\n")

                if rpta == 5:
                    break
                if rpta == 1:
                    for i in range(len(lec.clientela)):
                        print(lec.clientela[2].)
                        print(lec.usux)
                        print(lec.contx)
