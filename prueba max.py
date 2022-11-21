
from lecturacsv import csvclientes, clientela


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
