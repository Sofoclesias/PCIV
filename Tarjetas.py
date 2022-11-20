Tar = []

def verificacion(x):
    suma = 0
    if len(x) == 16:
        for r in range(len(x)):
            if r % 2 == 0:
                if int(x[r]) * 2 >= 10:
                    m = str(int(x[r]) * 2)
                    m = int(m[:1]) + int(m[1:])

                    suma = suma + m
                else:
                    suma = suma + int(x[r])
            else:
                suma = suma + int(x[r])
        if suma % 10:
            return ("la tareta a sido validada")
    else:
        return ("la tarjeta no existe")
def tarjetas():
    while True:
        while True:
            try:
                tarjeta = input("Ingrese los 16 caracteres de su tarjeta: ")
                print(verificacion(tarjeta))
                if verificacion(tarjeta) == "la tareta a sido validada":
                    break
                else:
                    print("escriba una tarjeta verdadera")
            except:
                print("escriba una tarjeta verdadera")
                pass
        Tar.append(tarjeta)
        while True:
            try:
                print("**** **** **** ", str(tarjeta)[-4:])
                print("¿Desea confirmar la tarjeta?")
                print("1. Sí")
                print("2. No")
                opc = int(input("escriba la opción: "))
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
        return tarjeta
