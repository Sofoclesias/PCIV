carritoprod = []
carritoext = []
precio = []
prod = [[1, "Pizza americana", 24.90], [2, "Pizza hawaiana", 26.90], [3, "Pizza suprema", 29.90],
        [4, "Pizza cuatro quesos", 28.90],
        [5, "Pizza de pepperoni", 27.90]]
extras = [[1, "tomate", 1.90], [2, "parmesano", 2.90], [3, "bbq", 3.90], [4, "anchoas", 5.90], [5, "piña", 4.90],
          [6, "chorizo", 4.90], [7, "jamón", 4.90], [8, "bordes de queso", 5.90], [9, "pepperoni", 5.90],
          [10, "champiñones", 6.90], [11, "salchicha", 7.90]]


def realizarpedidos():
    while True:
        while True:
            try:
                print("Menú Productos".center(31, "*"))
                print("{0:<4}{3}{1:<19}{3}{2:^6}".format("ID", "Productos", "Precios", "|"))
                for i in prod:
                    print("{0:<4}{3}{1:<19}{3}{2:>6}".format(i[0], i[1], i[2], "|"))
                print("si desea salir presione 0\n")
                opcprod = int(input("¿Qué producto desea ordenar? "))
                print("\n")
                if 0 <= opcprod <= len(prod):
                    if opcprod > 0:
                        print("¿cuantas unidades?")
                        while True:
                            try:
                                cantidad = int(input("ingrese la cantidad de pizzas"))
                                if cantidad > 0:
                                    break
                            except:
                                print("escriba una cantidad válida")
                        for i in prod:
                            if int(opcprod) == i[0]:
                                carritoprod.append([i[1], "{} unidades".format(cantidad)])
                                precio.append(round(i[2] * cantidad, 1))
                    break
                else:
                    print("ingrese una opción valida\n")
            except:
                print("ingrese una opcion válida\n")
        if opcprod == 0:
            break

    while True:
        while True:
            try:
                print("Menú Extras".center(31, "*"))
                print("{0:4}{3}{1:<19}{3}{2:^6}".format("ID", "Productos", "Precios", "|"))
                for i in extras:
                    print("{0:<4}{3}{1:<19}{3}{2:>6}".format(i[0], i[1], i[2], "|"))
                print("si desea salir presione 0\n")
                opcext = int(input("¿Qué extras desea añadir? "))
                print("\n")
                if 0 <= opcext <= len(extras):
                    if opcext > 0:
                        gramos = int(input("ingrese las unidades extras: "))
                        for i in extras:
                            if int(opcext) == i[0]:
                                carritoext.append([i[1], "{} unidades".format(gramos)])
                                precio.append(round(i[2] * gramos, 1))
                    break
                else:
                    print("ingrese una opción valida\n")
            except:
                print("ingrese una opcion válida\n")
        if opcext == 0:
            break
    print("Pizzas: ".center(50, "*"))
    for x in carritoprod:
        print("{0:<25}{1:^25}".format(x[0], x[1]))
    if len(carritoext) > 0:
        print(" Extras: ".center(50, "*"))
        for x in carritoext:
            print("{0:<25}{1:^25}".format(x[0], x[1]))
    print(" Precio total:", sum(precio))