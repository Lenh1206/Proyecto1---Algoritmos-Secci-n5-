from clase_asiento import Asiento
from clase_producto import Drink, Food
import itertools as itert

def age_validation(edad):
        if edad.isnumeric():
            return True
        else: 
            return False

def dni_validation(dni):
    if dni.isnumeric():
        if len(dni) >= 7 and len(dni) < 9:
            return True
        else:
            print('La cedula debe tener entre 7 y 8 digitos')
            return False
    else:
        print('La cedula debe ser númerica')
        return False

def is_perfect(id):
    id = int(id)
    divisores = []
    for elemento in range(id):
        if elemento != 0:
            if id % elemento == 0:
                divisores.append(elemento)
    if len(divisores) > 0:        
        if sum(divisores) == id:
            return True
        else:
            return False
    else:
        return False

def is_vampiric(id):
    if len(id) % 2 != 0:
        print(len(id) % 2)
        return False
    
    permutations = itert.permutations(id, len(id))
    for permutation in permutations:

        colmillo1 = permutation[:len(id)//2]
        colmillo2 = permutation[len(id)//2:]

        colmillo1 = ''.join(colmillo1)
        colmillo2 = ''.join(colmillo2) 
    
        if colmillo1[-1] == '0' and colmillo2[-1] == '0': 
            continue 
        if int(colmillo1)*int(colmillo2) == int(id):
            return True
    return False
  

def validate_id_of_game(id, lista_partidos):
    for partido in lista_partidos:
        if partido.id == id:
            return partido
    return None

def validar_disponibilidad(selected_partido):
    if selected_partido.disponibility['Total'] != 0:
        return True
    else:
        return False
    
def search_client(dni, lista_clientes):
    for client in lista_clientes:
        if client.dni == dni:
            return client
    return None


def crear_lista():
    return []

def asientos_estadio(asientos):
    lista_asientos = []
    codigo_asientos = []
    rango_total = range(asientos)
    for indice in rango_total:
        asiento = Asiento(codigo=f'O{indice}', estado='Libre')
        lista_asientos.append(asiento)
        codigo_asientos.append(asiento.code)
    return [lista_asientos, codigo_asientos]

def show_asientos(asientos_vip, asientos_generales):
    indice = 0
    asientos = []
    fila = []
    for asiento in range(len(asientos_vip)):
        if asiento / 10 == 0:
            asientos.append(fila)
            fila = []
        object_sit = Asiento(codigo=str(asiento), estado='Libre')
        if asiento / 10 != 0:
            fila.append(object_sit)
        else:
            next_fila = crear_lista()
            next_fila.append(object_sit)

def puede_comprar_bebidas(cliente, producto):
    if isinstance(producto, Drink):
        if producto.is_alcoholic == True and int(cliente.age) < 18:
            return False
        else:
            return True

def replace(sit):
    if sit.code.__contains__('O'):
        sit.code.replace('O', 'X')

