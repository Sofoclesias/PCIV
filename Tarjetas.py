Tar = []


def tarjetas():
    while True:
        tarjeta = input("Ingrese los 16 caracteres de su tarjeta: ")
        tarjeta4 = list(tarjeta)
        dig = tarjeta4[-4:]
        if len(tarjeta) == 16:
            Tar.append(tarjeta)
            print("Tarjeta añadida")
            print("**** **** **** ", dig)
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
                pass
        else:
            print("Ingrese un número válido")


tarjetas()
