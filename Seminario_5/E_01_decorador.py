def decorador(funcion):
    def interna(y):
        print "***", funcion(y), "***"

    return interna


@decorador

