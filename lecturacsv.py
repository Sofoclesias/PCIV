import clases as cl
import os
from datetime import *


def eliminarfilacsv(db, row):
    with open(db, 'r') as file:
        l = file.readlines()

    new_l = []
    for i in range(len(l)):
        if row == i:
            pass
        else:
            new_l.append(l[i])

    with open(db, 'w') as file:
        file.writelines(new_l)


def modificarvalorcsv(db, new_val, row, column):
    data = []
    with open(db, 'r') as file:
        l = file.readlines()
        for linea in l:
            data.append(linea.split(","))

    txt = ""
    for i in range(len(data[0]) - 1):
        if column == i:
            txt += str(new_val) + ","
        else:
            txt += str(data[row][i]) + ","
    txt += "\n"
    l[row] = txt

    with open(db, 'w') as file:
        file.writelines(l)

def actualizarcsv(db, new):
    txt = ""
    for i in range(len(new)):
        txt += str(new[i]) + ","
    txt += "\n"

    with open(db, 'r') as file:
        file.readlines()
    with open(db, 'a') as file:
        file.write(txt)

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
                    fven = str(mven).zfill(2) + "/" + str(yven)
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

        if sum(cardx) % 10 == 0 and card_type != None:
            print("¡Tarjeta identificada y registrada satisfactoriamente!")

            infocard = card_type + "|" + str(card) + "|" + "|" + fven + "|" + str(cvv)
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
    ix = None
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

                    modificarvalorcsv(csvclientes, clientela[i][8], i, 8)

                    flag = False
                    break
            if flag:
                print("No se ha encontrado al usuario. Inténtelo de nuevo.")
    print("¡Cuenta creada satisfactoriamente!")

    ## Creación de la clase
    x = cl.Cliente(dnix, nomx, apex, edx, usux, pasx, meth, 0, 0)
    clientela.append([dnix, nomx, apex, edx, usux, pasx, meth, 0, 0])

    actualizarcsv(csvclientes, [dnix, nomx, apex, edx, usux, pasx, meth, 0, 0])


csvclientes = os.path.dirname(os.path.realpath(__file__)) + '\db\clientes.csv'
csvadmin = os.path.dirname(os.path.realpath(__file__)) + '\db\ladmin.csv'
csvpizzas = os.path.dirname(os.path.realpath(__file__)) + '\db\pizzas.csv'
csvextras = os.path.dirname(os.path.realpath(__file__)) + '\db\extras.csv'
csvpedidos = os.path.dirname(os.path.realpath(__file__)) + '\db\pedidos.csv'

admin = excludecsvformat(copycsv(csvadmin))
clientela = excludecsvformat(copycsv(csvclientes))
prod = excludecsvformat(copycsv(csvpizzas))
extras = excludecsvformat(copycsv(csvextras))
pedidos = excludecsvformat(copycsv(csvpedidos))

for i in range(len(prod)):
    prod[i] = [int(prod[i][0]), prod[i][1], float(prod[i][2]), int(prod[i][3])]
for i in range(len(extras)):
    extras[i] = [int(extras[i][0]), extras[i][1], float(extras[i][2]), int(extras[i][3])]