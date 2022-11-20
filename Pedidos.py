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
                if opcprod <= len(prod):
                    for i in prod:
                        if int(opcprod) == i[0]:
                            carritoprod.append(i[1])
                            precio.append(i[2])
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
                if opcext <= len(extras):
                    for i in extras:
                        if int(opcext) == i[0]:
                            carritoext.append(i[1])
                            precio.append(i[2])
                    break
                else:
                    print("ingrese una opción valida\n")
            except:
                print("ingrese una opcion válida\n")
        if opcprod == 0:
            break
    print("Pizzas: ", carritoprod)
    print("Extras: ", carritoext)
    print("Precio:", sum(precio))
realizarpedidos()