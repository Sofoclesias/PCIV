import clases as cl
import pickle, os
import clientes as clic
from datetime import *
from administrativos import menu_admin


def copycsv(db):
    rows = []
    dbx = open(db, "r")
    for linea in dbx:
        rows.append(linea.split(","))
    dbx.close()
    return rows

def excludecsvformat(db):
    for i in range(len(db)):
        for j in range(len(db[0])):
            db[i][j] = db[i][j].rstrip(" ")
    return db

def refPago():
    infocard = None

    while True:
        while True:
            try:
                card = int(input("            Ingrese tarjeta de crédito: "))
                yven = int(input("           Ingresar año de vencimiento: "))
                mven = int(input("           Ingresar mes de vencimiento: "))
                fven = date(yven, mven, 1)
                cvv = int(input("           Ingresar CVV (máx 3 cifras): "))
                if fven > datetime.today().date() and len(str(cvv)) == 3:
                    fven = str(mven) + "/" + str(yven)
                    break
            except:
                print("Ingrese datos válidos.")

                op = input("¿Desea seguir intentando? (y/n): ").lower()
                if op == "y":
                    pass
                elif op == "n":
                    return infocard

        card = str(card)
        cardx = [int(x) for x in card]
        if cardx[0] == 4 and len(cardx) == 16:
            card_type = "Visa"
        elif cardx[0] == 5 and len(cardx) == 16:
            card_type = "MasterCard"
        elif cardx[0] == 3 and len(cardx) == 15:
            card_type = "American Express"
        else:
            card_type = None

        for i in range(2, len(cardx) + 1, 2):
            n = cardx[-i] * 2
            if n >= 10:
                n, add = str(n), 0
                for digit in n:
                    add += int(digit)
                n = add
            cardx[-i] = n

        if sum(cardx) % 10 == 0:
            print("¡Tarjeta identificada y registrada satisfactoriamente!")

            infocard = [card_type, card, fven, cvv]
            return infocard
        else:
            print("La tarjeta NO es válida.")

            op = input("¿Desea seguir intentando? (y/n): ").lower()
            if op == "y":
                pass
            elif op == "n":
                return infocard


def register():
    def tiene_numeros(string):
        return any(char.isdigit() for char in string)

    print('  BIENVENIDO NUEVO CLIENTE  '.center(50, '#'))

    ## DNI
    while True:
        try:
            dnix = int(input('\n                        Ingrese su DNI: '))
            break
        except:
            pass
    ## NOMBRES
    while True:
        try:
            nomx = input('                   Ingrese sus nombres: ').title()
            if tiene_numeros(nomx) == False:
                break
        except:
            pass
    ## APELLIDOS
    while True:
        try:
            apex = input('                 Ingrese sus apellidos: ').title()
            if tiene_numeros(apex) == False:
                break
        except:
            pass
    ## EDAD
    while True:
        try:
            edx = int(input('                       Ingrese su edad: '))
            break
        except:
            pass
    ## USUARIO
    while True:
        try:
            usux = input('Ingrese un usuario (mín. 3 caracteres): ')
            if len(usux) >= 3:
                flagUnico = True
                for i in range(len(clientela)):
                    if usux == clientela[i][4]:
                        flagUnico = False
                if flagUnico == True:
                    break
                else:
                    print("Ese usuario ya existe. Intenta otra opción.")
        except:
            pass
    ## CONTRASEÑA
    pasx = input('                Ingrese una contraseña: ')

    ## MÉTODO DE PAGO
    while True:
        quest = input("¿Desea agregar una forma de pago fija? (y/n): ")
        if quest == "y":
            meth = refPago()
            break
        elif quest == "n":
            meth = None
            break

    ## REFERIDO
    flag = True
    while flag == True:
        ref = input('Ingrese el usuario que le refirió sobre el sistema (de no haber, escribir "n"): ')
        if ref == "n":
            flag = False
            break
        if ref != "n":
            for i in range(len(clientela)):
                if ref == clientela[i][4]:
                    print("¡Cliente {} encontrado!".format(clientela[i][1]))
                    clientela[i][8] = int(clientela[i][8]) + 1

                    with open(csvclientes, 'r') as file:
                        data = file.readlines()

                    data[i] = "{0},{1},{2},{3},{4},{5},{6},{7},{8},\n".format(clientela[i][0], clientela[i][1],
                                                                              clientela[i][2],
                                                                              clientela[i][3], clientela[i][4],
                                                                              clientela[i][5],
                                                                              clientela[i][6], clientela[i][7],
                                                                              clientela[i][8])

                    with open(csvclientes, 'w') as file:
                        file.writelines(data)

                    flag = False
                    break
                else:
                    print("No se ha encontrado al usuario. Inténtelo de nuevo.")
    print("¡Cuenta creada satisfactoriamente!")

    ## Creación de la clase
    x = cl.Cliente(dnix, nomx, apex, edx, usux, pasx, meth, [], 0)
    clientela.append([dnix, nomx, apex, edx, usux, pasx, meth, [], 0])

    ## Agregar al csv
    baseclientes = open(csvclientes, 'a')
    baseclientes.write(
        '{0},{1},{2},{3},{4},{5},{6},0,0,\n'.format(dnix, nomx, apex, edx, usux, pasx, meth))
    baseclientes.close()


def login_cliente():
    print('  BIENVENIDO CLIENTE  '.center(50, '#'))

    flag = True
    while flag == True:
        global usux
        global contx
        usux = input('\n        Ingresa tu usuario: ')
        contx = input('     Ingresa tu contraseña: ')

        for i in range(len(clientela)):

            if usux == clientela[i][4] and contx == clientela[i][5]:
                nombre = 'BIENVENIDO ' + clientela[i][1].upper()
                flag = False
                break

        if flag == True: print('\n', 'Intenta de nuevo o contacta con el administrador'.center(50, '*'))

    print('\n', nombre.center(50), '\n')

    clic.menu_clientes()


def login_admin():
    print('  BIENVENIDO ADMINISTRADOR  '.center(50, '#'))

    flag = True
    while flag == True:
        dnix = input('\n            Ingresa tu DNI: ')
        contx = input('     Ingresa tu contraseña: ')

        for i in range(len(admin)):
            if dnix == admin[i][0] and contx == admin[i][4]:
                nombre = 'BIENVENIDO ' + admin[i][1].upper()
                flag = False
                break

        if flag == True: print('\n', 'Intenta de nuevo o contacta con el administrador'.center(50, '*'))

    print('\n', nombre.center(50), '\n')

    menu_admin(clientela)


def actualizar(db, new):
    data = open(db, 'rb')
    L = pickle.load(data)
    data.close()
    L.append(new)
    data = open(db, 'wb')
    pickle.dump(L, data)
    data.close()


usux = ""
contx = ""

csvclientes = os.path.dirname(os.path.realpath(__file__)) + '\db\clientes.csv'
csvadmin = os.path.dirname(os.path.realpath(__file__)) + '\db\ladmin.csv'
csvpizzas = os.path.dirname(os.path.realpath(__file__)) + '\db\pizzas.csv'
csvextras = os.path.dirname(os.path.realpath(__file__)) + '\db\extras.csv'

admin = excludecsvformat(copycsv(csvadmin))
clientela = excludecsvformat(copycsv(csvclientes))
prod = excludecsvformat(copycsv(csvpizzas))
extras = excludecsvformat(copycsv(csvextras))

for i in range(len(clientela)):
    clientela[i][6] = clientela[i][6].split("|")
for i in range(len(prod)):
    prod[i] = [int(prod[i][0]), prod[i][1], float(prod[i][2])]
for i in range(len(extras)):
    extras[i] = [int(extras[i][0]), extras[i][1], float(extras[i][2])]
