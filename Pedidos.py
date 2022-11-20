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
    print("Menú Productos".center(31, "*"))
    print("{0:<4}{3}{1:<19}{3}{2:^6}".format("ID", "Productos", "Precios", "|"))
    for i in prod:
        print("{0:<4}{3}{1:<19}{3}{2:>6}".format(i[0], i[1], i[2], "|"))

    while True:
        while True:

            try:
                print("si desea salir presiones 0")
                opcprod = int(input("¿Qué producto desea ordenar? "))
                if opcprod <= len(prod):
                    for i in prod:
                        if int(opcprod) == i[0]:
                            carritoprod.append(i[1])
                            precio.append(i[2])
                    break
                else:
                    print("ingrese una opción valida")
            except:
                print("ingrese una opcion válida")
        if opcprod == 0:
            break

    print("Menú Extras".center(31, "*"))
    print("{0:4}{3}{1:<19}{3}{2:^6}".format("ID", "Productos", "Precios", "|"))
    for i in extras:
        print("{0:<4}{3}{1:<19}{3}{2:>6}".format(i[0], i[1], i[2], "|"))
    print("Una vez terminado, escriba: salir")
    while True:
        opcext = input("¿Qué extras desea añadir? ")
        if opcext == i[0]:
            carritoext.append(extras[i][1])
            precio.append(extras[i][3])
        elif opcext == "salir":
            break
        else:
            print("Ingresar un codigo válido")
    print("Pizzas: ", carritoprod)
    print("Extras: ", carritoext)
    print("Precio:", sum(precio))
realizarpedidos()