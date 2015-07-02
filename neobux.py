def a_morado (n=1,tipo=0):
    """ Esta función calcula el valor de hacer n clicks en aun anuncio tipo
    morado o gris (micro) de neobux.
    n es un valor entero y es la cantidad de clicks
    tipo es un valor INT vale 1 si es gold 0 si es standar
    """
    if (tipo==0):
        return n*0.001
    else:
        return n*0.001

def a_naranja (n=1,tipo=0):
    """ Esta función calcula el valor de hacer n clicks en aun anuncio tipo
    naranja de neobux.
    n es un valor entero y es la cantidad de clicks
    tipo es un valor INT vale 1 si es gold 0 si es standar
    """
    if (tipo==0):
        return n*0.001
    else:
        return n*0.010
