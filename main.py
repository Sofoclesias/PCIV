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
        print('Registro')
    elif op == 2:
        print('''Portal de compras''')
    elif op == 3:
        print('''Portal de administradores''')
    elif op == 4:
        break
    else:
        print(' Ingresa una opcion del menú')
