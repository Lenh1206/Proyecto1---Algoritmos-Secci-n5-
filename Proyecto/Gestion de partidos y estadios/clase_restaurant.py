from clase_producto import Product, Food, Drink

class Restaurant():
    def __init__(self, nombre, lista_productos):
        self.name = nombre
        self.lista_productos = lista_productos

    def show_products(self):
        for producto in self.lista_productos:
            print(f'''\n
*****************************
Nombre: {producto.name}
Precio: {producto.price}
Disponibles: {producto.stock}
*****************************''')
        

    def return_sdd(self):
        return {'name':self.name,
'products':self.return_products_sdd()}
    
    def return_products_sdd(self):
        lista = []
        for product in self.lista_productos:
            sdd_products = product.return_sdd()
            lista.append(sdd_products)
        return lista
    