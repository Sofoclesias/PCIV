import lecturacsv as lec

print(lec.clientela[3][2])

lec.clientela[3][2] = "la verdad mera"
print(lec.clientela[3][2])


def muestra():
    for i in range(len(lec.clientela)):
        print(lec.clientela[i])


muestra()
