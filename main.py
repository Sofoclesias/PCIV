from lecturacsv import register, login_cliente, login_admin

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
