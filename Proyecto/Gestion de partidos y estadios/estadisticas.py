import gestion_estadios as gest_stad
import log_clients as log
from log_clients import lista_clientes, lista_tickets
import gestion_partidos as gest_rounds
from gestion_estadios import lista_estadios
from gestion_partidos import lista_partidos, lista_asientos_partidos
import venta_restaurantes as rest_sells
import gestion_asistencia as gest_asists

def persons_with_most_tickets(lista_clientes, lista_tickets):
    checkeds = []
    times = []
    if len(lista_tickets)>0:
        for index, ticket in enumerate(lista_tickets):
            if ticket.cliente not in checkeds:    
                temp = ticket.cliente
                x=0
                for elements in lista_tickets[index:]:
                    if elements.cliente == temp:
                        x +=1
                times.append((x, temp))
                checkeds.append(ticket.cliente)
        rank = sorted(times)
        rank = rank[::-1]
        cont = 0
        for cliente in lista_clientes:
            if cont <=3:    
                if cliente.dni == rank[0][1]:
                    print(f'El cliente con mas boletos comprados es {cliente.name}, con un total de {rank[0][0]}')
                    cont+=1
    else:
        print('Nadie ha comprado boletos.')

def ranking_asistencias(lista_partidos, search):
    ranking = []
    tuplas = []
    checkeds = []
    for partido in lista_partidos:
        asistencias = 0
        if len(partido.tickets_registrados) > 0:
            for ticket in partido.tickets_registrados:
                if ticket.status == 'Claimed':
                    asistencias += 1
            partido_y_info = (asistencias, partido.id)
            tuplas.append(partido_y_info)
        else:
            partido_y_info = (asistencias, partido.id)
            tuplas.append(partido_y_info)
    tuplas = sorted(tuplas)
    ranking = tuplas[::-1]
    if search == 'General':
        for element in ranking:
            print(f'Partido: {element[1]} - Asistencias totales: {element[0]}')
        print('')
    if search == 'Top1':
        print(f'Partido: {ranking[0][1]} - Asistencias totales: {ranking[0][0]}')
        print('')
                
    
def partido_mayor_venta_tickets(lista_entradas):
    ranking = []
    tuplas = []
    checkeds = []
    if len(lista_entradas) > 0:
        for ticket in lista_entradas:
            ticket_to_compare = ticket.match
            tuplas.append(ticket_to_compare)

        for index, ticket in enumerate(tuplas):
            if ticket not in checkeds:    
                temp = ticket
                checkeds.append(temp)
                x=0
                for elements in tuplas[index:]:
                    if elements == temp:
                        x +=1   
                ranking.append((x, ticket))
        ranking = sorted(ranking)
        top = ranking[::-1]
        print(f'Partido con mayor venta de boletos: {top[0][1]} ---- Boletos vendidos: {top[0][0]}')
    else:
        print('Entre todos los partidos no se han vendido tickets.')
    

def promedio_de_gastos(lista_clientes, partido, lista_estadios):
    clientes_vip = 0
    selected_stadium = None
    promedio_gastos_restaurantes = None
    for ticket in partido.tickets_registrados:
        if ticket.is_vip == True:
            clientes_vip += 1
        for estadio in lista_estadios:
            if ticket.match.stadium == estadio.id:
                selected_stadium = estadio
    if selected_stadium:
        for restaurant in selected_stadium.restaurants:
            pass
    else:
        print('No se encontro un estadio asociado.')

def top_3_productos(restaurante):
    ranking = []
    for producto in restaurante.lista_productos:
        ranking.append((producto.times_selled, producto.name))
    ranking = sorted(ranking)
    top_3 = ranking[::-1]
    cont = 0
    for veces_vendido, producto in top_3:
        if cont <= 2:
            print(f'Nombre: {producto} - Vendido: {veces_vendido} veces')
            cont += 1

def stadistic_options(lista_partidos, lista_entradas, lista_estadios, lista_clientes):
    while True:
        option = input('''\n¿Que estadisticas desea consultar?:
                    
1. Promedio de gastos de clientes VIP 
2. Ranking de asistencias
3. Partido con mayor asistencia
4. Partido con mayor venta de boletos
5. Top 3 productos más vendidos (Restaurantes) 
6. Top 3 clientes con boletos comprados
7. Salir
->''')
        if option == '1':
            pass
            '''for partido in lista_partidos:
                print('**********************')
                print(partido.details())
            opcion = input('Indique el partido señalando su id: ').lower()
            selected_match = None
            for partido in lista_partidos:
                if partido.id.lower() == opcion:
                    selected_match = partido
            if selected_match:
                promedio_de_gastos(lista_clientes, partido, lista_estadios)
            else:
                print('No se encontro dicho partido.')'''
        elif option == '2':
            ranking_asistencias(lista_partidos, 'General')
        elif option == '3':
            ranking_asistencias(lista_partidos, 'Top1')
        elif option == '4':
            partido_mayor_venta_tickets(lista_entradas)
        elif option == '5':
            selected_restaurant = None
            opcion = input('Indique el estadio donde se encuentra indicando su id: ')
            selected_stadium = gest_stad.search_stadium(opcion, lista_estadios)
            if selected_stadium:
                print('\nSeleccione el restaurante\n')
                gest_stad.show_specific_stadium_restaurant(selected_stadium)
                opcion = input('->').lower()
                for restaurant in selected_stadium.restaurants:
                    if restaurant.name.lower() == opcion:
                        selected_restaurant = restaurant
                if selected_restaurant:
                    top_3_productos(selected_restaurant)
                else:
                    print('No se encontro un restaurante con dicho nombre.')
            else:
                print('No se encontro.') 
        elif option == '6':
            persons_with_most_tickets(lista_clientes, lista_tickets)
        elif option == '7':
            break
        else:
            print('No corresponde a ninguna de las opciones..')