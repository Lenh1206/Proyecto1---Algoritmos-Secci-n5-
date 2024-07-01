class Product():
    def __init__(self, nombre, cantidad_vendida, price, stock, adicional, times_selled):
        self.name = nombre
        self.quantity = cantidad_vendida
        self.price = price
        self.stock = stock
        self.adicional = adicional
        self.times_selled = times_selled

    def show_product_info(self):
        return f'''Nombre: {self.name}
Vendidos: {self.quantity}
Precio: {self.price}
Stock: {self.stock}
Adicional: {self.adicional}'''
    
    def return_sdd(self):
        return {'name':self.name,
'quantity':self.quantity,
'price':self.price[0],
'stock':self.stock,
'adicional':self.adicional,
'veces_vendida':self.times_selled}

class Food(Product):
    def __init__(self, nombre, cantidad_vendida, price, stock, adicional, times_selled, is_package):
        super().__init__(nombre, cantidad_vendida, price, stock, adicional, times_selled)
        self.is_package = is_package


class Drink(Product):
    def __init__(self, nombre, cantidad_vendida, price, stock, adicional, times_selled, is_alcoholic):
        super().__init__(nombre, cantidad_vendida, price, stock, adicional, times_selled)
        self.is_alcoholic = is_alcoholic



    