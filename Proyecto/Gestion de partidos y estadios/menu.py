import gestion_estadios as gest_stad
import log_clients as log
from log_clients import lista_clientes, lista_tickets
import gestion_partidos as gest_rounds
from gestion_estadios import lista_estadios
from gestion_partidos import lista_partidos, lista_asientos_partidos, lista_equipos
import venta_restaurantes as rest_sells
import gestion_asistencia as gest_asists
import estadisticas as estadistic
import funciones_go_back as save

def menu():
    print('''**********************************************
        BIENVENIDO A LA EUROCOPA 2024
**********************************************''')
    while True:
        '''for cliente in lista_clientes:
            print(cliente.dni)'''
        print('''\n¿Que desea realizar?
              
1. Venta de entradas
2. Gestionar partidos y estadios
3. Gestionar asistencias
4. Gestionar un restaurante
5. Gestionar Ventas de un Restaurante
6. Ver estadisticas
7. Salir del sistema''')
        option = input('\n->')
        if option == '1':
            log.vender_entrada(lista_clientes, lista_partidos, lista_asientos_partidos, lista_tickets)
        elif option == '2':
            gest_rounds.choose_filter_rounds()
        elif option == '3':
            ticket = input('Introduzca el codigo del ticket: ')
            gest_asists.check_in(ticket, lista_tickets)
        elif option == '4':
            gest_stad.show_stadiums_info(lista_estadios)
            opcion = input('Indique el estadio donde se encuentra indicando su id: ')
            selected_stadium = gest_stad.search_stadium(opcion, lista_estadios)
            if selected_stadium:
                gest_stad.gest_rest.gestion_restaurantes(selected_stadium)
            else:
                print('No se encontro.')
        elif option == '5':
            selected_restaurant = None
            opcion = input('Indique el estadio donde se encuentra indicando su id o nombre: ')
            selected_stadium = gest_stad.search_stadium(opcion, lista_estadios)
            if selected_stadium:
                print('\nSeleccione el restaurante indicando su nombre: \n')
                gest_stad.show_specific_stadium_restaurant(selected_stadium)
                opcion = input('->').lower()
                for restaurant in selected_stadium.restaurants:
                    if restaurant.name.lower() == opcion.lower():
                        selected_restaurant = restaurant
                if selected_restaurant:
                    rest_sells.realizar_compra(lista_clientes, selected_restaurant, lista_tickets)
                else:
                    print('No se encontro un restaurante con dicho nombre.')
            else:
                print('No se encontro.') 
        elif option == '6':
            estadistic.stadistic_options(lista_partidos, lista_tickets, lista_estadios, lista_clientes)
        elif option == '7':
            save.return_all(lista_partidos, lista_estadios, lista_equipos, lista_clientes, lista_tickets, lista_asientos_partidos)
            break
        else:
            if option.isalpha():
                print('\nDebe introducir un número correspondiente a los otorgados')
            else:
                print('\nLa respuesta introducida no corresponde a ninguna de las opciones.')

#1234555

menu()

