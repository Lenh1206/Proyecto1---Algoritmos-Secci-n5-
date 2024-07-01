from gestion_estadios import lista_estadios, objects_stadium
from gestion_partidos import lista_partidos, lista_equipos, object_rounds, lista_asientos_partidos
from log_clients import lista_clientes, lista_tickets
from APIS.AllApis import partidos, estadios, equipos
import json

def return_all(lista_partidos, lista_estadios, lista_equipos, lista_clientes, lista_tickets, lista_asientos):

    new_partidos = return_dict_matches(lista_partidos)
    archivo_partidos = open('Gestion de partidos y estadios/lista_partidos.txt', 'w')
    json.dump(new_partidos, archivo_partidos)

    new_stadiums = return_dict_stadiums(lista_estadios)
    archivo_estadios = open('Gestion de partidos y estadios/lista_estadios.txt', 'w')
    json.dump(new_stadiums, archivo_estadios)

    new_clients = return_dict_clientes(lista_clientes)
    archivo_clientes = open('Gestion de partidos y estadios/lista_clientes.txt', 'w')
    json.dump(new_clients, archivo_clientes)

    new_teams = return_dict_teams(lista_equipos)
    archivo_equipos = open('Gestion de partidos y estadios/lista_equipos.txt', 'w')
    json.dump(new_teams, archivo_equipos)

    new_tickets = return_dict_tickets(lista_tickets)
    archivo_tickets = open('Gestion de partidos y estadios/lista_tickets.txt', 'w')
    json.dump(new_tickets, archivo_tickets)

    archivo_asientos = open('Gestion de partidos y estadios/lista_asientos.txt', 'w')
    json.dump(lista_asientos, archivo_asientos)

    


def return_dict_matches(lista_partidos):
    new_lista_partidos = []
    for partido in lista_partidos:
        new_partido = partido.return_sdd()
        new_lista_partidos.append(new_partido)
    return new_lista_partidos

def return_dict_stadiums(lista_estadios):
    new_lista_estadios = []
    for estadio in lista_estadios:
        new_estadio = estadio.return_to_sdd()
        new_lista_estadios.append(new_estadio)
    return new_lista_estadios

def return_dict_teams(lista_equipos):
    new_teams_list = []
    for equipo in lista_equipos:
        new_team = equipo.return_to_sdd()
        new_teams_list.append(new_team)
    return new_teams_list

def return_dict_clientes(lista_clientes):
    new_clients_list = []
    if len(lista_clientes)>0:
        for cliente in lista_clientes:
            new_cliente = cliente.return_sdd()
            new_clients_list.append(new_cliente)
        return new_clients_list
    else:
        return new_clients_list

def return_dict_tickets(lista_tickets):
    new_tickets_list = []
    if len(lista_tickets)>0:
        for ticket in lista_tickets:
            new_ticket = ticket.return_sdd()
            new_tickets_list.append(new_ticket)
        return new_tickets_list
    else:
        return new_tickets_list





    