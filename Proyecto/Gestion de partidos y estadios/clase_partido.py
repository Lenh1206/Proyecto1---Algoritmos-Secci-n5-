from clase_equipo import Equipo
from clase_estadio import Estadio

class Partido():
    def __init__(self, id, number, home, away, date, group, stadium_id, disponibilidad, tickets_registrados) -> None:
        self.id = id
        self.number = number
        self.home = home
        self.away = away
        self.date = date
        self.group = group
        self.stadium = stadium_id
        self.disponibility = disponibilidad
        self.tickets_registrados = tickets_registrados
    
    def show_match(self):
        return f'''{self.id}
{self.number}
{self.home.name}
{self.away.name}
{self.stadium.name}
'''
    def details(self):
        return f'''Estadio: {self.stadium.name} id: {self.id}
Detalles:

Disponibilidad: {self.disponibility['Total']}
{self.home.name} vs {self.away.name}

Partido #{self.number}
Fecha: {self.date}
Grupo: {self.group}
'''
    def return_sdd(self):
        return {'id' : self.id,
'number': self.number,
'home': self.home.return_to_sdd(),
'away': self.away.return_to_sdd(),
'date': self.date,
'group': self.group,
'stadium_id': self.stadium.id,
'tickets':self.return_tickets_sdd()
}
    
    def return_tickets_sdd(self):
        lista = []
        if len(self.tickets_registrados) > 0:
            for ticket in self.tickets_registrados:
                lista.append(ticket.return_sdd())
            return lista
        else:
            return lista

    def contar_tickets_vendidos(self):
        cont = 0
        if len(self.tickets_registrados) > 0:
            for ticket in self.tickets_registrados:
                cont +=1
            return cont
        return 0