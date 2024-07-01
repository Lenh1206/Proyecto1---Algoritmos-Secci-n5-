import gestion_restaurants as gest_rest
from gestion_partidos import lista_partidos
from log_clients import registrar_cliente
from log_clients import lista_clientes
import validations as valid
from clase_producto import Food, Drink

def factura(cliente, lista_productos):
    print('Productos:')
    checkeds = []
    total = 0.00
    for producto, cantidad in lista_productos:
        print(f'\n{producto.name} x ({cantidad}) ---- {producto.price})')
    for producto, cantidad in lista_productos:
        calculo = (float(producto.price[0])*cantidad).__round__(2)
        total += calculo
        discount = 0.00
        if valid.is_perfect(cliente.dni):
            discount = 0.15
            print('\nEl cliente aplica para un descuento especial, ya que su cedula es un número perfecto.')
    print(f'''\nDescuento: {discount}
Sub_total: {total}
Total: {total-(total*discount)}''')

def show_products_selected(lista_productos):
    print('\nLos productos seleccionados son:')
    for producto, cantidad in lista_productos:
        print(f'''\n*************
{producto.name}
{producto.price[0]} x {cantidad}
*************''')

def calculate_price(cliente, lista_productos):
    total = 0.00
    for producto, cantidad in lista_productos:
        print(producto.price, type(producto.price))
        print(cantidad, type(cantidad))
        total += (float(producto.price[0])*cantidad).__round__(2)
    return total

def seleccionar_productos(cliente, restaurante, back_up):
    selected_products = []
    print(restaurante.show_products())
    while True:
        option = input('\nSeleccione el producto indicando su nombre o coloque 0 para terminar la operación: ')
        if option != '0':
            for producto in back_up:
                selected_product = None
                if producto.name.lower() == option.lower():
                    if producto.stock != 0:
                        if isinstance(producto, Drink):
                            if valid.puede_comprar_bebidas(cliente, producto) == True:
                                selected_product = producto
                                cantidad = input('\n¿Cuantas unidades de este producto desea comprar?: ')
                                if cantidad.isnumeric() == True:
                                    if producto.stock >= int(cantidad):
                                        selected_products.append((selected_product, int(cantidad)))
                                        print('Producto agregado con exito.\n')
                                        break
                                    else:
                                        print('\nLa cantidad deseada excede la cantidad disponible del producto.')
                                else:
                                    print('\nLas cantidades deben expresarse con números enteros.')
                            else:
                                print('No puede comprar esta bebida ya que es menor de edad\n') 
                        else:
                            selected_product = producto
                            cantidad = input('\n¿Cuantas unidades de este producto desea comprar?: ')
                            if cantidad.isnumeric() == True:
                                if producto.stock >= int(cantidad):
                                    selected_products.append((selected_product, int(cantidad)))
                                    print('Producto agregado con exito.\n')
                                    break
                                else:
                                        print('\nLa cantidad deseada excede la cantidad disponible del producto.')
                            else:
                                print('Las cantidades deben expresarse con números enteros.')       
                    else:
                        print('El producto se encuentra agotado. Seleccione otro.')
            if selected_product == None:
                print('No se encontro un producto con el nombre indicado.\n')
        else:
            'print(back_up)'
            for producto in restaurante.lista_productos:
                print(producto.show_product_info())
                print('')
            '''for producto_rest in restaurante.lista_productos:
                for producto_back in back_up:
                    if producto_rest.name == producto_back.name:
                        producto_rest.stock = producto_back.stock'''
            break
    return selected_products

def realizar_compra(lista_clientes, restaurante, lista_tickets):
    while True:
        cedula = input('\nIntroduzca la cédula del cliente: ')
        if valid.dni_validation(cedula) == True:
            break
    cliente = valid.search_client(cedula, lista_clientes)
    if cliente:
        ticket_to_evaluate = []
        for ticket in lista_tickets:
            if ticket.cliente == cliente.dni:
                ticket_to_evaluate.append(ticket)
        if len(ticket_to_evaluate) > 0:
            valido = False
            for ticket in ticket_to_evaluate:
                if ticket.is_vip == True:
                    valido = True
                    break
            if valido == True:
                productos = seleccionar_productos(cliente, restaurante, restaurante.lista_productos)
                if productos:
                    '''for productos_rest in restaurante.lista_productos:
                        print(productos_rest.show_product_info())'''
                    total = calculate_price(cliente, productos)
                    show_products_selected(productos) 
                    print(f'El total a pagar es: {total}') 
                    option = input('¿Desea continuar? (Y/N)\n').upper()
                    if option == 'Y':
                        for producto in restaurante.lista_productos:
                            for selected, cantidad in productos:
                                if producto.name.lower() == selected.name.lower():
                                    if producto.stock - cantidad >= 0:
                                        producto.stock -= cantidad
                                        producto.times_selled += cantidad
                                        print('\nCompra realizada con exito.\nFactura:')
                                        factura(cliente, productos) 
                                    else:
                                        print(f'\nLa cantidad de producto {selected.name} que se introdujo excede con la cantidad disponible en el stock. ')      
                    else:
                        print('\nSe cancelo la compra.')          
                else:
                    print('\nNo se seleccionaron productos.')
            else:
                print('Solo los clientes VIP, pueden acceder al restaurante.')
        else:
            print('El cliente no cuenta con un ticket.')
    else:
        print('El cliente no se encuentra registrado.') 
        

