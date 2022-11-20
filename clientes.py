import clases as cl
import lecturacsv as lec
import Tarjetas as tarj


def menu_clientes():
    for i in range(len(lec.clientela)):
        if lec.usux == lec.clientela[i][4] and lec.contx == lec.clientela[i][5]:
            cliente_creacion = cl.Cliente(lec.clientela[i][0], lec.clientela[i][1], lec.clientela[i][2],
                                          lec.clientela[i][3]
                                          , lec.clientela[i][4], lec.clientela[i][5])
    while True:
        while True:
            try:

                print("{0:^10} {1:^10} {2:^10} {3:^10}".format("DNI", "NOMBRE", "APELLIDO", "EDAD"))
                print("{0:^10} {1:^10} {2:^10} {3:^10}".format(cliente_creacion.getDNI(), cliente_creacion.getNombres()
                                                               , cliente_creacion.getApellidos(),
                                                               cliente_creacion.getEdad()))

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
                    cliente_creacion.setnumero_de_cuenta(tarj.tarjetas())
