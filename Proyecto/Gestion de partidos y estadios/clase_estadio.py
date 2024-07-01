from clase_restaurant import Restaurant

class Estadio():
    def __init__(self, id, nombre, ubicacion, capacidad, restaurantes):
        self.id = id
        self.name = nombre
        self.city = ubicacion
        self.capacidad = capacidad
        self.restaurants = restaurantes


    def show_restaurants(self):
        for restaurant in self.restaurants:
            print(f'Nombre: {restaurant.name}')
            
    def return_to_sdd(self):
        return {'id':self.id,
'name':self.name,
'city':self.city,
'capacity':self.capacidad['Both'],
'restaurants':self.return_sdd_restaurants()}
    
    def return_sdd_restaurants(self):
        lista = []
        for restaurant in self.restaurants:
            sdd_restaurant = restaurant.return_sdd()
            lista.append(sdd_restaurant)
        return lista