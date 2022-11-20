Tar = []


def tarjetas():
    while True:
        tarjeta = int(input("Ingrese los 16 caracteres de su tarjeta: "))
        if len(str(tarjeta)) == 16:
            Tar.append(tarjeta)
            print("Tarjeta añadida")
            print("**** **** **** ", str(tarjeta)[-4:])
            print("¿Desea confirmar la tarjeta?")
            print("1. Sí")
            print("2. No")
            opc = input("")
            if opc == "1":
                print(Tar)
                break
            elif opc == "2":
                Tar.remove(tarjeta)
                print(Tar)
            else:
                print("Ingrese una respuesta válida")
                Tar.remove(tarjeta)
        else:
            print("Ingrese un número válido")


tarjetas()
