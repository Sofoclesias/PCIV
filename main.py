from lecturacsv import *
from administrativos import menu_admin
import clientes as clic



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

    clic.menu_clientes(usux, contx)


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

    menu_admin()


usux = ""
contx = ""

print('  BIENVENIDO  '.center(50, '#'))
while True:
    op = int(input('''
    1. Registro
    2. Portal de compras
    3. Portal administrativo
    4. Salir

    Selecciona tu opción: '''))
    print('\n', '#' * 50)
    if op == 1:
        register()
    elif op == 2:
        login_cliente()
    elif op == 3:
        login_admin()
    elif op == 4:
        break
    else:
        print(' Ingresa una opcion del menú')