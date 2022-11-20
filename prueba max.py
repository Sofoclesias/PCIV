import lecturacsv as lec
import clases as cl

for i in range(len(lec.clientela)):
    if "axels" == lec.clientela[i][4] and "1234" == lec.clientela[i][5]:
        cliente_creacion = cl.Cliente(lec.clientela[i][0], lec.clientela[i][1], lec.clientela[i][2],
                                      lec.clientela[i][3]
                                      , lec.clientela[i][4], lec.clientela[i][5])
print(cliente_creacion.apellidos)
print(cliente_creacion.getApellidos())
print(cliente_creacion.setApellidos("huamanga"))
print(cliente_creacion.apellidos)
print(cliente_creacion.getApellidos())
