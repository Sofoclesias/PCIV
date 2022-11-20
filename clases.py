from datetime import *
class Personas:
    def __init__(self, dnix, nomx, apex, edx):
        self.DNI = dnix
        self.nombres = nomx
        self.apellidos = apex
        self.edad = edx

    def getDNI(self):
        return self.DNI

    def setDNI(self, DNIx):
        self.DNI = DNIx

    def getNombres(self):
        return self.nombres

    def setNombres(self, nomx):
        self.nombres = nomx

    def getApellidos(self):
        return self.apellidos

    def setApellidos(self, apex):
        self.apellidos = apex

    def getEdad(self):
        return self.edad

    def setEdad(self, edx):
        self.edad = edx


class Pizzero(Personas):
    def __init__(self, dnix, nomx, apex, edx, contx):
        super().__init__(dnix, nomx, apex, edx)
        self.password = contx

    def getPassword(self):
        return self.password

    def setPassword(self, refx):
        self.password = refx


class Cliente(Personas):
    def __init__(self, dnix, nomx, apex, edx, usux, contx, meth, pedx, refx):
        super().__init__(dnix, nomx, apex, edx)
        self.usuario = usux
        self.contraseña = contx
        self.metodoPago = pedx
        self.ref = refx

    def getRef(self):
        return self.ref

    def setRef(self, refx):
        self.ref = refx

    def getnumero_de_cuenta(self):
        return self.numero_de_cuenta

    def setnumero_de_cuenta(self, nuevo_numero_de_cuenta):
        self.numero_de_cuenta = nuevo_numero_de_cuenta
