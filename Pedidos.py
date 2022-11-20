prod = [["Pizza americana", 24.90], ["Pizza hawaiana", 26.90], ["Pizza suprema", 29.90], ["Pizza cuatro quesos", 28.90],
        ["Pizza de pepperoni", 27.90]]
prod1 = ["Pizza americana", "Pizza hawaiana", "Pizza suprema", "Pizza cuatro quesos",
         "Pizza de pepperoni"]
extras = ["tomate", "anchoas", "piña", "bbq", "bordes de queso"]

for i in prod:
    print("{0:<19}{1:^19}".format(i[0], i[1]))
def realizarpedidos():
    print("Menú".center(28, "*"))
    for i in prod:
        print("{0}".format(prod[i][0]))


realizarpedidos()
