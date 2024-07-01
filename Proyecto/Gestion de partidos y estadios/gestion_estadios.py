from APIS.AllApis import estadios
from clase_estadio import Estadio
import gestion_restaurants as gest_rest
from clase_asiento import Asiento

########################################################################################################################
#FUNCIONES PRINCIPALES



#1)FUNCION TRANSFORMAR OBJETO

def objects_stadium(estadios):
    object_stadiums = []
    for estadio in estadios:
        capacidad1 = estadio['capacity'][0]
        capacidad2 = estadio['capacity'][1]
        generals = capacidad1
        vips = capacidad2
        capacidades_stadium = {'Total':generals+vips,'General':generals, 'VIP':vips, 'Both':estadio['capacity']}
        stadium = Estadio(id=estadio['id'], nombre=estadio['name'], ubicacion=estadio['city'], capacidad=capacidades_stadium, restaurantes=estadio['restaurants'])
        stadium.restaurants = gest_rest.transform_restaurants(stadium)
        object_stadiums.append(stadium)
    return object_stadiums



########################################################################################################################
#FUNCIONES DE BUSQUEDA:


#1) MOSTRAR INFORMACIÓN DE CADA ESTADIO
def show_stadiums_info(lista_estadios):
    for estadio in lista_estadios:
        print('')
        print(f'-Nombre: {estadio.name}')
        print(f'id: {estadio.id}')
        print('')



#2) MOSTRAR RESTAURANTES DE CADA ESTADIO
def show_stadiums_restaurants(lista_estadios):
    for estadio in lista_estadios:
        print(f'{estadio.name}\n')
        print(f'{estadio.restaurants.name}\n')

def show_specific_stadium_restaurant(estadio):
    for restaurante in estadio.restaurants:
        print(f'-{restaurante.name}')


#3) BUSCAR ESTADIO EN PARTICULAR 
def search_stadium(valor, lista_estadios):
    for stadium in lista_estadios:
        if stadium.id.lower() == valor.lower() or stadium.name.lower() == valor.lower(): #Se modifico el nombre de la funcion y su alcance, de modo que se pueda buscar no solo por id sino por nombre
            return stadium
    return None



#########################################################################################################################
#FUNCION DE ASIENTOS DE ESTADIOS


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
    '''
    Aqui se organiza la disposición de las listas de asientos de modo que se muestren 
    en listas de len == 10.
    '''
    gen = []
    cont = 0   
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

def create_each_stadiums_sits(lista_estadio):
    '''
    Crea los asientos de cada estadio de acuerdo a su capacidad VIP y General.
    '''
    lista_asientos = []
    for estadio in lista_estadio:
        stadium_sits = {'id' : estadio.id,
        'VIP' : create_list_sits(estadio.capacidad['VIP'], 'vip'),
        'General':create_list_sits(estadio.capacidad['General'], 'gen')}
        lista_asientos.append(stadium_sits)
    return lista_asientos


#4) MOSTRAR ASIENTOS
            
def show_stadium_sits(estadio, lista_asientos, tipo_entrada):
    for lista_asientos in lista_asientos_partidos:
        if lista_asientos['id'] == estadio.id:
            print(f'''Estadio: {estadio.name}

Asientos {tipo_entrada} disponibles:
{lista_asientos[tipo_entrada]}''')      

            
#5) CAMBIAR ESTADO A OCUPADO

def change_state(choosed, lista_asientos):
    for asiento in lista_asientos:
        if asiento == choosed:
            asiento = choosed.replace('O', 'X')  #MODIFICAR DE MODO QUE LA LISTA DE ASIENTO SEA LA LISTA DEL ESTADIO EN ESPECIFICO
            return asiento

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
    for asiento in lista_asientos:
        if asiento.__contains__(choosed):
            return asiento

def search_stadiums_list(estadio, lista_asientos, tipo):
    for lista_asiento in lista_asientos:
        if lista_asiento['id'] == estadio.id:
            return lista_asiento[tipo]


lista_estadios = objects_stadium(estadios) 
lista_asientos_partidos = create_each_stadiums_sits(lista_estadios)






