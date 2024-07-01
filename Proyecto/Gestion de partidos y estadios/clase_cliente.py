class Client():
    def __init__(self, nombre, cedula, edad, partido, tipo_entrada, asiento):
        self.name = nombre
        self.dni = cedula
        self.age = edad
        self.ticket = tipo_entrada
        self.game = partido
        self.sit = asiento

    def return_sdd(self):
        return {'name':self.name,
'dni':self.dni,
'age':self.age,
'ticket':self.ticket,
'game':self.game.return_sdd(),
'sit':self.sit}
