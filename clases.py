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
        self.password = contx


class Cliente(Personas):
    def __init__(self, dnix, nomx, apex, edx, usux, contx):
        super().__init__(dnix, nomx, apex, edx)
        self.usuario = usux
        self.contraseña = contx
        self.ref = 0

    def getRef(self):
        return self.ref

    def setRef(self, refx):
        self.ref = refx
