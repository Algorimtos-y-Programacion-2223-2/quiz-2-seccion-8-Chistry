class Edificio:
    def __init__(self, nombre, pisos, calle, ciudad, codigo_postal):
        self.nombre =nombre
        self.pisos =pisos
        self.calle =calle
        self.ciudad =ciudad
        self.codigo_postal =codigo_postal

    def mostrar_apartamento(self):
        return f'Nombre:{self.nombre}\nPisos:{self.pisos}\nCalle:{self.calle}\nCiudad:{self.ciudad}\nCodigo Postal:{self.codigo_postal}\n'
    def mostrar_direccion(self):
        return f'Calle:{self.calle}\nCiudad:{self.ciudad}\nCodigo Postal:{self.codigo_postal}\n'
