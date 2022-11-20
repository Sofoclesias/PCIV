Tar = []
def tarjetas():
    while True:
        while True:
            try:
                tarjeta = input("Ingrese los 16 caracteres de su tarjeta: ")
                if int(tarjeta) > 0 and len(tarjeta) == 16:
                    break
                else:
                    print("escriba una tarjeta verdadera")
            except:
                print("escriba una tarjeta verdadera")
                pass
        if len(str(tarjeta)) == 16:
            Tar.append(tarjeta)
            while True:
                try:
                    print("**** **** **** ", str(tarjeta)[-4:])
                    print("¿Desea confirmar la tarjeta?")
                    print("1. Sí")
                    print("2. No")
                    opc = int(input(""))
                    if str(opc) in "12":
                        break
                    else:
                        print("escriba una opcion válida")
                except:
                    print("escriba una opción valida")

            if opc == 1:
                break
            elif opc == 2:
                Tar.remove(tarjeta)
                print(Tar)
            else:
                print("Ingrese una respuesta válida")
                Tar.remove(tarjeta)
        else:
            print("Ingrese un número válido")
    return tarjeta
