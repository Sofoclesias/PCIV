prod = ["Pizza americana", "Pizza hawaiana", "Pizza suprema", "Pizza cuatro quesos", "Pizza de pepperoni"]
extra = ["tomate", "anchoas", "piña", "bbq", "bordes de queso"]


def realizarpedidos():
    print("Menú".center(28, "*"))
    for x in prod:
        print("{}")


realizarpedidos()
