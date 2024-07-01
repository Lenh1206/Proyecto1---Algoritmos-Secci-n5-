'''from APIS.API_equipos import equipos
from APIS.API_partidos import partidos'''
from clase_partido import Partido
from clase_equipo import Equipo

from APIS.AllApis import equipos, partidos, asientos
from gestion_estadios import lista_estadios, show_stadiums_info
import datetime 

def insert_date():
    fecha = input('''Introduzca una fecha con el siguente formato: (yy/mm/dd)
->''')
    try:
        format_fecha = datetime.datetime.strptime(fecha, '%Y/%m/%d').date() 
        return str(format_fecha)
    except ValueError:
        print('Fecha o formato invalido')


def objetc_equipos(equipos):
    object_teams = []
    for equipo in equipos:
        object_team = Equipo(id=equipo['id'], code=equipo['code'], group=equipo['group'], name=equipo['name'])
        object_teams.append(object_team)
    return object_teams

def object_rounds(partidos, lista_equipos, lista_estadios): #Falta anexar la funcion de los estadios
    object_partidos = []
    for partido in partidos:
        for estadio in lista_estadios:
            if partido['stadium_id'] == estadio.id:
                stadium = estadio 
        for equipo in lista_equipos:
            if partido['home']['id'] == equipo.id:
                home = equipo
            if partido['away']['id'] == equipo.id:
                away = equipo
        object_partido = Partido(id=partido['id'], number=partido['number'], home=home, away=away, date=partido['date'], group=partido['group'], stadium_id=stadium, disponibilidad=stadium.capacidad, tickets_registrados=[])     
        object_partidos.append(object_partido) 
    return object_partidos

def search_pais(pais, lista_equipos):
    for equipo in lista_equipos:
        if equipo.name.lower() == pais:
            return equipo
    return None

#######################################################################################################################

def search_by_country(lista_partidos):
    rounds_of_country = []
    opcion = input('Introduzca el pais a buscar: ').lower()
    pais = search_pais(opcion, lista_equipos)
    if pais:
        for partido in lista_partidos:
            if partido.home == pais:
                rounds_of_country.append(partido)
            elif partido.away == pais:
                rounds_of_country.append(partido)
        if len(rounds_of_country) == 0:
            print('El equipo no tiene partidos programados')
        else: 
            for round in rounds_of_country:
                print('\n************************')
                print(round.details())
            print('************************')
    else:
        print('Pais no encontrado.')

def search_by_stadium(lista_estadios, lista_partidos):
    rounds_in_stadium = []
    estadio_selected = None
    show_stadiums_info(lista_estadios)
    opcion = input('\nSeleccione un estadio: ').lower()
    for estadio in lista_estadios:
        if estadio.name.lower() == opcion:
            estadio_selected = estadio
    if estadio_selected:
        for partido in lista_partidos:
            if partido.stadium == estadio_selected:
                rounds_in_stadium.append(partido)
        if len(rounds_in_stadium) < 1:
            print('\nEl estadio no tiene partidos programados\n')
        else:
            print('\nPartidos programados:\n')
            for partido in rounds_in_stadium:
                print(partido.details())
    else:
        opcion = input('Estadio no encontrado, desea intentarlo denuevo o volver al menu? (Y/N)').upper()
        if opcion == 'Y':
            search_by_stadium(lista_estadios)

def search_by_date(lista_partidos):
    coincidencias = []
    print('Introduzca una fecha, tome el siguiente ejemplo como referencia: (01/02/2024)')
    fecha = insert_date()
    if fecha:
        for partido in lista_partidos:
            if partido.date == fecha:
                coincidencias.append(partido)
        if len(coincidencias) < 1:
            print(f'No se encontraron partidos para el {fecha}')
        else:
            print(f'\nLos partidos disponibles para el {fecha} son:')
            for partido in coincidencias:
                print('\n************************')
                print(partido.details())   
                print('************************')    
    else:
        option = input('''¿Desea reintentarlo? (Y/N)
->''').upper()    
        if option == 'Y':
            insert_date()

#######################################################################################################################

def search_rounds(filtro, lista_partidos, lista_equipos, lista_estadios):
    if filtro == '1': #Por país
        search_by_country(lista_partidos)

    elif filtro == '2': #Por estadio
        search_by_stadium(lista_estadios, lista_partidos)

    elif filtro == '3': #Por Fecha
        search_by_date(lista_partidos)

#######################################################################################################################

def show_rounds(lista_partidos):
    for partido in lista_partidos:
        print(f'\n{partido.details()}')

def choose_filter_rounds():
    while True:
        option = input('''¿Que opción de busqueda desea ejecutar? (Si desea terminar ingrese 0)
1. Por pais
2. Por estadio
3. Por fecha
0. Volver al menu
->''')
        if option == '1':
            search_rounds(option, lista_partidos, lista_equipos, lista_estadios)
            print('')
        elif option == '2':
            search_rounds(option, lista_partidos, lista_equipos, lista_estadios)
            print('')
        elif option == '3':
            search_rounds(option, lista_partidos, lista_equipos, lista_estadios)
            print('')
        elif option == '0':
            break
        else:
            print('No corresponde a ninguna de las opciones otorgadas.')
            option = input('¿Desea reintentar? (Y/N)').upper()
            if option == 'N':
                break

lista_equipos = objetc_equipos(equipos)
lista_partidos = object_rounds(partidos, lista_equipos, lista_estadios)



#1) OBJETAR LOS ASIENTOS Y ANEXARLOS A UNA LISTA
def asientos_estadio(capacidad, type):
    lista_asientos = []
    rango_total = range(capacidad)
    for indice in rango_total:
        if type == 'vip':
            asiento = f'Ov{indice}'
            lista_asientos.append(asiento)
        else:
            asiento = f'Og{indice}'
            lista_asientos.append(asiento)
    return lista_asientos

#2) CREAR LOS ASIENTOS EN FUNCIÓN DE LA CANTIDAD

def create_list_sits(capacidad, type):
    asientos = asientos_estadio(capacidad, type)
    return asientos

#3) CREAR ASIENTOS DE CADA ESTADIO

def organizar_lista_asientos(lista):
    gen = []
    cont = 0   #MODIFICAR DE MODO QUE MODIFIQUE LOS ASIENTOS INTERNOS
    temp = 0
    for index, ele in enumerate(lista):
        if cont==10:
            gen.append(list(lista[temp:index]))
            temp = index
            cont = 0
        cont+=1
    if lista[temp] != lista[-1]:
        gen.append(list(lista[temp:]))
    return gen

def create_each_match_sits(lista_partidos):
    lista_asientos = []
    for partido in lista_partidos:
        stadium_sits = {'id' : partido.id,
        'VIP' : organizar_lista_asientos(create_list_sits(partido.stadium.capacidad['VIP'], 'vip')),
        'General':organizar_lista_asientos(create_list_sits(partido.stadium.capacidad['General'], 'gen'))}
        lista_asientos.append(stadium_sits)
    return lista_asientos


#4) MOSTRAR ASIENTOS
'''def show_stadium_sits(estadio, lista_asientos, tipo_entrada):
    for lista_asientos in lista_asientos_estadio:
        if lista_asientos['id'] == estadio.id:
            print(fEstadio: {estadio.name}

Asientos {tipo_entrada} disponibles:
{lista_asientos[tipo_entrada]})'''
            
'''def show_partido_sits(partido, lista_asientos, tipo_entrada):
    for lista_asientos in lista_asientos_partidos:
        if lista_asientos['id'] == partido.id:
            print(fPartido: {partido.id}

Asientos {tipo_entrada} disponibles:
{lista_asientos[tipo_entrada]}) '''

def show_partido_sits(lista_asientos):
    for lista_interna in lista_asientos:
        print(lista_interna)
        print('')    

            
#5) CAMBIAR ESTADO A OCUPADO
  
def change_state(choosed, lista_asientos):
    for lista_interna in (lista_asientos):
        for index, asiento in enumerate(lista_interna):
            if asiento == choosed:
                modified = choosed.replace('O', 'X')  #MODIFICAR DE MODO QUE LA LISTA DE ASIENTO SEA LA LISTA DEL ESTADIO EN ESPECIFICO
                lista_interna[index] = modified
                return lista_asientos

#6) VERIFICAR SI ESTA OCUPADO

def verify_is_valid(choosed):
    if choosed.isnumeric() == False:
        return False
    else:
        return True
    
def verify_is_available(choosed, lista_asientos):
    if choosed.__contains__('O'):
        return True
    elif choosed.__contains__('X'):
        return False

def search_sit(choosed, lista_asientos):
    for lista_interna in lista_asientos:
        for asiento in lista_interna:
            if asiento.__contains__(choosed):
                return asiento

def search_partidos_list(partido, lista_asientos, tipo):
    for lista_asiento in lista_asientos:
        if lista_asiento['id'] == partido.id:
            return lista_asiento[tipo]

if len(asientos) == 0:
    lista_asientos_partidos = create_each_match_sits(lista_partidos)
else:
    lista_asientos_partidos = asientos


'''lista_asientos_partidos = create_each_match_sits(lista_partidos)'''