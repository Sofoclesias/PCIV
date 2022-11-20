
from lecturacsv import csvclientes, clientela


def modificarcsv(db, local_list, new_val, row, column):
    with open(db, 'r') as file:
        data = file.readlines()

    txt = ""
    for i in range(len(local_list[0]) - 1):
        if column == i:
            txt += str(new_val) + ","
        else:
            txt += str(local_list[row][i]) + ","

        print(txt)
    txt += "\n"

    data[row] = txt

    with open(csvclientes, 'w') as file:
        file.writelines(data)


modificarcsv(csvclientes, clientela, 3, 0, 8)
