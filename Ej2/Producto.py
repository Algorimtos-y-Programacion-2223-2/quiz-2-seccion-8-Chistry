class Producto:
    def __init__(self, id, name, tipo, stock, price):
        self.id =id
        self.name =name
        self.tipo =tipo
        self.stock =stock
        self.price =price
    def mostrar(self):
        return f'ID:{self.id}\nNombre:{self.name}\nTipo:{self.tipo}\nStock:{self.stock}\nPrecio:{self.price}\n'
    