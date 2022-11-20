from lecturacsv import register, login_cliente, login_admin

print('  BIENVENIDO  '.center(50, '#'))
while True:
    while True:
        try:
            op = int(input('''
            1. Registro
            2. Portal de compras
            3. Portal administrativo
            4. Salir
        
            Selecciona tu opción: '''))
            if str(op) in "1234":
                break
            else:
                print("ingrese una opción correcta")
        except:
            print("ingrese una opción correcta")
            pass
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
