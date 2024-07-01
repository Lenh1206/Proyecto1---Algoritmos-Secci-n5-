from clase_restaurant import Restaurant
from clase_producto import Food, Drink



def apply_iva(precio, status):
    if status == 'Sin iva':
        float_price = float(precio)
        price_with_iva = str(round((float_price + (float_price*0.16)), 2))
        status = 'Con iva'
        return [price_with_iva, status]
    else:
        return[precio, status]




########################################################################################################################
#FUNCION PRINCIPAL:



#1) TRANSFORMAR A OBJETOS - FUNCION INTERNA PARA GESTION DE ESTADI
def transform_restaurants(estadio):
    restaurants_list = []
    for restaurant in estadio.restaurants: 
        products_list = []
        for product in restaurant['products']:
            if product['adicional'] == 'alcoholic' or product['adicional'] == 'non-alcoholic':
                if product['adicional'] == 'alcoholic':
                    object_product = Drink(nombre=product['name'], cantidad_vendida=product['quantity'], price=apply_iva(product['price'], 'Sin iva'), stock=product['stock'], adicional=product['adicional'], is_alcoholic=True, times_selled=0)
                    products_list.append(object_product)
                elif product['adicional'] == 'non-alcoholic':
                    object_product = Drink(nombre=product['name'], cantidad_vendida=product['quantity'], price=apply_iva(product['price'], 'Sin iva'), stock=product['stock'], adicional=product['adicional'], is_alcoholic=False, times_selled=0)
                    products_list.append(object_product)
            else:
                if product['adicional'] == 'package':
                    object_product = Food(nombre=product['name'], cantidad_vendida=product['quantity'], price=apply_iva(product['price'], 'Sin iva'), stock=product['stock'], adicional=product['adicional'], is_package=True, times_selled=0)
                    products_list.append(object_product)
                else:
                    object_product = Food(nombre=product['name'], cantidad_vendida=product['quantity'], price=apply_iva(product['price'], 'Sin iva'), stock=product['stock'], adicional=product['adicional'], is_package=False, times_selled=0)
                    products_list.append(object_product)
        object_restaurant = Restaurant(nombre=restaurant['name'], lista_productos=products_list)
        restaurants_list.append(object_restaurant) 
    return restaurants_list



########################################################################################################################
#FUNCIONES DE BUSQUEDA DE OBJETOS 



#1) POR NOMBRE
def search_by_name(opcion, restaurant):
    products_searched = []
    for producto in restaurant.lista_productos:
        if producto.name.lower() == opcion.lower():
            producto_found = producto
            products_searched.append(producto_found)
    if len(products_searched) < 1:
        print(f'No se encontraron productos con el nombre: {opcion}')
    else:
        print('Aqui esta la información: ')
        for product in products_searched:
            print(f'\n{product.show_product_info()}\n')



#2) POR CATEGORIA (COMIDA O BEBIDA)
def search_by_category(opcion, restaurant):
    if opcion == 'Food':
        food_products = []
        for product in restaurant.lista_productos:
            if isinstance(product, Food):
                food_products.append(product)
        if len(food_products) < 1: 
            print('\nNo hay productos en esta categoria.')
        else:
            for product in food_products:
                print(f'\n{product.show_product_info()}')
    elif opcion == 'Drink':
        drink_products = []
        for product in restaurant.lista_productos:
            if isinstance(product, Drink):
                drink_products.append(product)
        if len(drink_products) < 1: 
            print('\nNo hay productos en esta categoria.')
        else:
            for product in drink_products:
                print(f'\n{product.show_product_info()}')
    else:
        print('\nNo existe una categoria correspondiente...')



#3) POR RANGO DE PRECIO
def search_by_price(rango, restaurants):
    coincidencias = []
    for product in restaurants.lista_productos:
        if float(product.price[0]) >= rango[0] and float(product.price[0]) < rango[1]:
            coincidencias.append(product)
    if len(coincidencias) < 1:
        print('No se hallaron coincidencias')
    else:
        for producto in coincidencias:
            print(f'{producto.show_product_info()}')
            




########################################################################################################################
#BUSQUEDA DE PRODUCTOS DE UN RESTAURANTE - USA FUNCIONES DE BUSQUEDA



def search_products(restaurant):
    while True: 
        option = input('''\nSeleccione una opción de busqueda:
1. Por nombre
2. Por tipo de producto
3 Por precio
4. Terminar la busqueda
->''')
        if option == '1':
            nombre = input('\nIntroduzca el nombre del producto: ')
            search_by_name(nombre, restaurant)
        elif option == '2':
            categorias = {'1': 'Food', '2': 'Drinks'}
            opcion = input('''Seleccione una de las siguiente categorias:
1. Comida
2. Bebidas
->''')
            if opcion == '1' or opcion == '2':
                search_by_category(categorias['opcion'], restaurant)
            else:
                print('Categoria no encontrada.')
        elif option == '3':
            ranges = {'1': [0.00, 100.00], '2': [100.00, 200.00], '3': [200.00, 400.00], '4': [400.00, 600.00], '5': [600.00, 1000.00], '6': [1000.00]}
            rango = input('''Seleccione un rango de busqueda:
1. De 0 a 100
2. De 100 a 200
3. De 200 a 400
4. De 400 a 600
5. De 600 a 1000
->''')
            if rango.isnumeric():
                if rango == '1' or rango == '2' or rango == '3' or rango == '4' or rango == '5':
                    selected_rango = None
                    for index in ranges.keys():
                        if rango == index:
                            selected_rango = ranges[index]
                    if selected_rango:
                        search_by_price(selected_rango, restaurant)
                    else:
                        print('No se selecciono un rango')
                else:
                    print('Opción no valida')
            else:
                print('La opción debe ser un númerica')
        elif option == '4':
            break
        else:
            print('No corresponde a ninguna de las opciones otorgadas\n')




########################################################################################################################
#SELECCIÓN DE RESTAURANTE A GESTIONAR


def gestion_restaurantes(stadium):
    while True:
        if stadium:
            selected_restaurant = None
            print(stadium.name)
            print(f'\n{stadium.show_restaurants()}')
            option = input('Seleccione un restaurante indicando su nombre o coloque 0 para regresar al menú anterior: ')
            if option != '0':
                for restaurant in stadium.restaurants:
                    if restaurant.name.lower() == option.lower():
                        selected_restaurant = restaurant
                if selected_restaurant != None:
                    search_products(selected_restaurant)
                else:
                    option = input('No se encontro un restaurante con el nombre indicado, ¿Desea intentarlo denuevo? (Y/N)').upper()
                    if option == 'N':
                        break
            else:
                break
        else:
            option = input('No se encontro el estadio indicado, ¿Desea intentarlo denuevo? (Y/N): ').upper()
            if option == 'N':
                break

########################################################################################################################
