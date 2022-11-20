
from lecturacsv import csvclientes


def actualizarcsv(db, new):
    txt = ""
    for i in range(len(new)):
        txt += str(new[i]) + ","
    txt += "\n"

    with open(db, 'r') as file:
        file.readlines()
    with open(db, 'a') as file:
        file.write(txt)


actualizarcsv(csvclientes, [0, 1, 2, 3, 4, 5, 6, 7, 8])
