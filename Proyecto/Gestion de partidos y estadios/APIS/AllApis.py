import requests
import json

api_partidos = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json'
api_estadios = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json'
api_equipos = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json'

'''partidos = requests.get(api_partidos).json()
estadios = requests.get(api_estadios).json()
equipos = requests.get(api_equipos).json()'''


try: 
    with open('Gestion de partidos y estadios/lista_partidos.txt', 'r') as origin_partidos:
        partidos = json.load(origin_partidos)

    with open('Gestion de partidos y estadios/lista_estadios.txt', 'r') as origin_estadios:
        estadios = json.load(origin_estadios)

    with open('Gestion de partidos y estadios/lista_equipos.txt', 'r') as origin_equipos:
        equipos = json.load(origin_equipos)

    with open('Gestion de partidos y estadios/lista_clientes.txt', 'r') as origin_clientes:
        clientes = json.load(origin_clientes)

    with open('Gestion de partidos y estadios/lista_tickets.txt', 'r') as origin_tickets:
        tickets = json.load(origin_tickets)
    
    with open('Gestion de partidos y estadios/lista_asientos.txt', 'r') as origin_asientos:
        asientos = json.load(origin_asientos)

except FileNotFoundError:

    partidos = requests.get(api_partidos).json()
    estadios = requests.get(api_estadios).json()
    equipos = requests.get(api_equipos).json()
    asientos = []
    clientes = []
    tickets = []











'''try: 
    with open('Gestion de partidos y estadios/lista_estadios.txt', 'w+') as origin_estadios:
        estadios = origin_estadios.read()

    with open('Gestion de partidos y estadios/lista_partidos.txt', 'w+') as origin_partidos:
        partidos = origin_partidos.read()

    with open('Gestion de partidos y estadios/lista_equipos.txt', 'w+') as origin_equipos:
        equipos = origin_equipos.read()

    with open('Gestion de partidos y estadios/lista_clientes.txt', 'w+') as origin_clientes:
        clientes = origin_clientes.read()

    with open('Gestion de partidos y estadios/lista_tickets.txt', 'w+') as origin_tickets:
        tickets = origin_tickets.read()
except FileNotFoundError:
    
    partidos = requests.get(api_partidos).json()
    estadios = requests.get(api_estadios).json()
    equipos = requests.get(api_equipos).json()
'''