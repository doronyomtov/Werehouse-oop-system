class Product:
    ID = 0

    def __init__(self, name, description, quantity, location):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.location = location
        Product.ID += 1
        self.sku = f'PROD{Product.ID}'

    def __str__(self):
        return f'{self.sku},{self.name},{self.description},{self.quantity},  {self.location}'

    def __repr__(self):
        return f'{self.sku},{self.name},{self.description},{self.quantity},{self.location}'
