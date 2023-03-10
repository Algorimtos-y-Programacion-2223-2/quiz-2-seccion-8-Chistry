from Edificio import Edificio
class App:
    def __init__(self):
        self.lista_apartamentos = []

    def metodo_contructor(self):
        try:
            nombre= input('Dime tu nombre?: ')
            if nombre == nombre.isalpha():
                raise ValueError
            pisos= int(input('Cual es tu piso?: '))
            calle= input('Dime la calle del edificio?: ')
            ciudad= input('En que ciudad esta el edificio?: ')
            codigo_postal= int(input('Cual es el nro del codigo postal donde se ubica el edificio?: '))
        except ValueError:
            print('Pon un valor valido e intentalo de nuevo')
        datos_edificio= Edificio(nombre, pisos, calle, ciudad, codigo_postal)
        self.lista_apartamentos.append(datos_edificio)


    def mostrar_apartamentos(self):
        for i in self.lista_apartamentos:
            print(Edificio.mostrar_apartamento(i))
    def mostrar_direccion(self):
        for i in self.lista_apartamentos:
            print(Edificio.mostrar_direccion(i))
    