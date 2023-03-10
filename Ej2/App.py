from Producto import Producto
class App():
    def __init__(self):
        self.lista_productos= {
            'hogar':[],
            'ropa':[],
            'gaming':[],
        }
        self.lista_producto=[]

    def organizar(self):
        products = [
            { "id": 1,"name":"Nevera", "type":"Hogar","stock": 753,"price": 800 },
            {"id": 2,"name":"Cama", "type":"Hogar","stock": 327,"price": 600 },
            {"id": 3,"name":"Suéter", "type":"Ropa","stock": 260,"price": 25 },
            {"id": 4,"name":"Zapatos", "type":"Ropa","stock": 593,"price": 5 },
            {"id": 5,"name":"Laptop Gamer", "type":"Gaming","stock": 11,"price": 2500 },
            {"id": 6,"name":"Nintendo Switch OLED", "type":"Gaming","stock": 25,"price": 400 },
            ]
        
        for i in products:
            producto=Producto(i["id"],i["name"],i["type"],i["stock"],i["price"])
            self.lista_producto.append(producto)
            if i["type"]=="Hogar":
                self.lista_productos['hogar'].append(producto)
            elif i["type"]=="Ropa":
                self.lista_productos['ropa'].append(producto)
            elif i["type"]=="Gaming":
                self.lista_productos['gaming'].append(producto)

    def mostrar(self):
        print('Lista de productos:')
        # for i in self.lista_producto:
        #     print(Producto.mostrar(i))
        for key,value in self.lista_productos.items():
            for i in value:
                if key == 'hogar':
                    print("Producto para el hogar:")
                    print(Producto.mostrar(i))
                elif key == 'ropa':
                    print("Producto relacionado con la ropa:")
                    print(Producto.mostrar(i))
                elif key == 'gaming':
                    print("Producto para el GAMING:")
                    print(Producto.mostrar(i))
    
