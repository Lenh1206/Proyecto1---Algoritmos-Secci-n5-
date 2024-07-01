from clase_cliente import Client
from clase_entrada import Entrada
import validations as v
from gestion_partidos import search_rounds, show_rounds, lista_partidos
import gestion_estadios as gest_stad
import gestion_partidos as gest_part
from gestion_estadios import lista_asientos_partidos
from APIS.AllApis import clientes, tickets

def search_client_by_dni(dni, lista_clientes):
    if len(lista_clientes) > 0:
        for cliente in lista_clientes:
            if dni == cliente.dni:
                return cliente

def choose_sit(tipo, estadio, lista_asientos):
    sits_of_stadium = gest_stad.search_stadiums_list(estadio, lista_asientos, tipo)
    gest_stad.show_stadium_sits(estadio, lista_asientos, tipo)
    while True:
            opcion = input('''\nSeleccione un asiento introduciendo el número correspondiente. 
(Ejemplo: Asiento: Og-123  Opción: 123): ''')
            if gest_stad.verify_is_valid(opcion) == True:
                asiento = gest_stad.search_sit(opcion, sits_of_stadium)
                if asiento:
                    if gest_stad.verify_is_available(asiento, sits_of_stadium) == True:
                        break
                    else:
                        print('\nEl asiento ya se encuentra ocupado, puede ver si esta libre si tiene la letra O al comienzo.')
                else:
                    print('No se encontro un asiento con el número indicado')
            else:
                print('El asiento debe indicarse por medio del número seguido del guión (-).')
    return asiento 

def choose_sit(tipo, partido, lista_asientos):
    sits_of_partido = gest_part.search_partidos_list(partido, lista_asientos, tipo)
    'print(sits_of_partido)'
    gest_part.show_partido_sits(sits_of_partido)
    while True:
            opcion = input('''\nSeleccione un asiento introduciendo el número correspondiente. 
(Ejemplo: Asiento: Og-123  Opción: 123): ''')
            if gest_part.verify_is_valid(opcion) == True:
                asiento = gest_part.search_sit(opcion, sits_of_partido)
                if asiento:
                    if gest_part.verify_is_available(asiento, sits_of_partido) == True:
                        break
                    else:
                        print('\nEl asiento ya se encuentra ocupado, puede ver si esta libre si tiene la letra O al comienzo.')
                else:
                    print('No se encontro un asiento con el número indicado')
            else:
                print('El asiento debe indicarse por medio del número seguido del guión (-).')
    return asiento          

def registrar_cliente(lista_clientes, lista_partidos):
    tipo_de_entradas = {'1': 'General', '2': 'VIP'}
    while True:
        cedula = input('Introduzca la cedula del cliente: ')
        if cedula.isnumeric():
            if v.dni_validation(cedula) == True:
                break
        else:
            print('La cedula debe ser númerica')
    if cedula:
        cliente = search_client_by_dni(cedula, lista_clientes)
        if cliente:
            nombre = cliente.name
            edad = cliente.age
        else:
            while True:
                nombre = input('Nombre del cliente: ')
                if nombre:
                    break
                else:
                    print('\nDebe ingresar un nombre valido')
            while True:
                edad = input('Edad: ')
                if v.age_validation(edad) == True:
                    break
                else:
                    print('La edad debe ser expresada en números enteros. Intetelo denuevo')   
    else:
        print('No se ingreso ninguna cedula...')

    for partido in lista_partidos:
        print('\n**********************')
        print(partido.details())

    while True:
        option = input('\nSeleccione el partido al que desea asistir señalando su id: ').lower()
        selected_game = v.validate_id_of_game(option, lista_partidos)
        if selected_game:
            if v.validar_disponibilidad(selected_game) == True:    
                break
            else:
                print('El partido se encuentra a su máxima capacidad. Seleccione otro juego')
        else:
            print('No se encontro un partido con la id arrojada. Intentelo denuevo.')
    if selected_game:
        while True:
            option = input('''\n¿Que tipo de entrada desea comprar? 
1. General
2. VIP
->''')
            if option == '1':
                tipo_de_entrada = tipo_de_entradas['1']
                break
            elif option == '2':
                tipo_de_entrada = tipo_de_entradas['2']
                break
            else:
                print('\nNo corresponde a ninguna de las opciones otorgadas.')
        if tipo_de_entrada:
            cliente = Client(nombre=nombre, cedula=cedula, edad=edad, partido=selected_game, tipo_entrada=tipo_de_entrada, asiento='Por Asignar')
            return cliente
        else:
            print('No se selecciono un tipo de entrada...')
    else:
        print('No se selecciono un partido...')

def calculate_price(cliente):
    if cliente:
        descuento = None
        if v.is_vampiric(cliente.dni) == True:
            print('\nEl numero de cedula es un número vampiro, se le aplicará un 50%. de descuento')
            descuento = 0.50
        else:
            descuento = 0
        if descuento:
            if cliente.ticket == 'VIP':
                precio_entrada = 75
                precio_con_iva = precio_entrada+(precio_entrada*0.16)
                total = precio_con_iva - (precio_con_iva*descuento)
            else:
                precio_entrada = 35
                precio_con_iva = precio_entrada+(precio_entrada*0.16)
                total = precio_con_iva - (precio_con_iva*descuento)
            print(f'''Precio de entrada = {precio_entrada}
Precio + IVA = {precio_con_iva}
Total a pagar = {total}''')
    else:
        print('\nNo hay un cliente.')


   
def vender_entrada(lista_clientes, lista_partidos, lista_asientos, lista_tickets):
    cliente = registrar_cliente(lista_clientes, lista_partidos)
    if cliente:
        is_vipp = None
        partido = cliente.game
        tipo = cliente.ticket
        if tipo == 'VIP':
            is_vipp = True
        else:
            is_vipp = False
        selected_asiento = choose_sit(tipo, partido, lista_asientos)
        if selected_asiento:
            calculate_price(cliente)
            while True:
                option = input('''\nDesea realizar la transacción? (Y/N)
->''').upper()
                if option == 'Y':
                    print(f'''Transacción realizada con exito!
El codigo de su asientos es: {selected_asiento}''')
                    for lista in lista_asientos:
                        if lista['id'] == partido.id:
                            actualizada = gest_part.change_state(selected_asiento, lista[tipo]) 
                            lista[tipo] = actualizada
                    cliente.sit = selected_asiento
                    lista_clientes.append(cliente)
                    partido.disponibility['Total'] -= 1 
                    partido.disponibility[tipo] -=1
                    entrada = Entrada(id=cliente.dni+cliente.sit+str(cliente.game.number), cliente=cliente.dni, asiento=cliente.sit, fecha=cliente.game.date, partido=cliente.game.id, is_vip=is_vipp, status='Unclaimed')
                    partido.tickets_registrados.append(entrada)
                    lista_tickets.append(entrada)
                    print(f'Su ticket es: {entrada.id}')
                    break
                else:
                    option = input('\nUsted selecciono que no desea continuar con la compra. ¿Esta seguro? (Y/N): ').upper()
                    if option == 'Y':
                        break       
        else:
            print('No se selecciono un asiento')
    else:
        print('No se registro un cliente')


def transform_object_clients(lista_clientes):
    obj_lista_clientes = []
    if len(lista_clientes) > 0:
        for cliente in lista_clientes:
            obj_client = Client(nombre=cliente['name'], cedula=cliente['dni'], edad=cliente['age'], partido=cliente['game']['id'], tipo_entrada=cliente['ticket'], asiento=cliente['sit'])
            obj_lista_clientes.append(obj_client)
        return obj_lista_clientes
    else:
        return obj_lista_clientes
    
def transform_object_tickets(lista_tickets):
    obj_lista_tickets = []
    if len(lista_tickets) > 0:
        for ticket in lista_tickets:
            obj_ticket = Entrada(id=ticket['id'], cliente=ticket['client_id'], asiento=ticket['sit'], fecha=ticket['date'], partido=ticket['game'], is_vip=ticket['is_vip'], status=ticket['status'])
            obj_lista_tickets.append(obj_ticket)
        return obj_lista_tickets
    else:
        return obj_lista_tickets


lista_clientes = transform_object_clients(clientes)
lista_tickets = transform_object_tickets(tickets)