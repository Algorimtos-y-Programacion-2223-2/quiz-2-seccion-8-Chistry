from App import App
def main():
    repetidor=True
    app= App()
    app.organizar()
    while repetidor:
        try:
            pregunta= int(input('Que quieres hacer?:\n1.Ordenar otra vez \n2.Ver producto\n3.Salir\n'))
        except ValueError:
            print('pon un valor valido')
        if pregunta ==1:
            app.organizar()
        elif pregunta==2:
            app.mostrar()
        elif pregunta==3:
            repetidor=False
main()