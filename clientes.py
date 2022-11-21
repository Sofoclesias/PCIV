import clases as cl
import lecturacsv as lec
import Tarjetas as tarj
import Pedidos as ped

def menu_clientes(usuario, contraseña):
    for i in range(len(lec.clientela)):
        if lec.usux == lec.clientela[i][4] and lec.contx == lec.clientela[i][5]:
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
                while True:
                    try:
                        print("{0:^10} {1:^10} {2:^10} {3:^10}".format("DNI", "NOMBRE", "APELLIDO", "EDAD"))
                        print("{0:^10} {1:^10} {2:^10} {3:^10}".format(cliente_creacion.getDNI(),
                                                                       cliente_creacion.getNombres()
                                                                       , cliente_creacion.getApellidos(),
                                                                       cliente_creacion.getEdad()))
                        rpta = int(input("¿que desea hacer?\n"
                                         "1.cambiar metodo de pago\n"
                                         "2.cambiar DNI\n"
                                         "3.cambiar nombre\n"
                                         "4.cambiar apellidos\n"
                                         "5.cambiar edad\n"
                                         "6.salir\n"
                                         "ingrese una opción: "))
                        if str(opcion) in "12345":
                            break
                        else:
                            print("escriba una opción correcta\n")
                    except:
                        print("escriba una opción correcta\n")

                if rpta == 6:
                    break
                if rpta == 1:
                    cliente_creacion.setnumero_de_cuenta(tarj.tarjetas())
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
                    cliente_creacion.setDNI(nuevo_dni)
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
                    cliente_creacion.setNombres(nuevo_nombre)
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
                    cliente_creacion.setApellidos(nuevo_apellido)
                if rpta == 5:
                    while True:
                        try:
                            nuevo_dni = int(input("ingrese la nueva edad: "))
                            if nuevo_dni >= 18:
                                break
                            else:
                                print("escriba una edad válida")
                        except:
                            print("escriba una edad válida")
                    cliente_creacion.setEdad(nuevo_dni)

        if opcion == 2:
            ped.realizarpedidos()
