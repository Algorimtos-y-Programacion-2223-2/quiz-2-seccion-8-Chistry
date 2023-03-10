from App import App

def main():
    repetidor=True
    app=App()
    app.metodo_contructor()
    while repetidor:
        try:
            pregunta= int(input('Que quieres hacer:\n1-Ver Aparatamentos\n2.Ver direccion de apartamentos\n3.Quieres agregar otro apartamento?\n4.SALIR\n'))
        except ValueError:
            print('Pon un valor valido')
        if pregunta ==1:
            app.mostrar_apartamentos()
        elif pregunta ==2:
            app.mostrar_direccion()
        elif pregunta ==3:
            app.metodo_contructor()
        elif pregunta ==4:
            repetidor=False

main()