def a_morado (n=1,tipo=0):
    """ Esta función calcula el valor de hacer n clicks en aun anuncio tipo
    morado o gris (micro) de neobux.
    n es un valor entero y es la cantidad de clicks
    tipo es un valor INT vale 1 si es gold 0 si es standar
    """
    if (tipo==0):
        click = 0.001
    else:
        click = 0.001
    return n * click

def a_naranja (n=1,tipo=0):
    """ Esta función calcula el valor de hacer n clicks en aun anuncio tipo
    naranja de neobux.
    n es un valor entero y es la cantidad de clicks
    tipo es un valor INT vale 1 si es gold 0 si es standar
    """
    if (tipo==0):
        click = 0.001
    else:
        click = 0.010
    return n * click

def r_a_naranja (n=1,tipo_r=0,tipo_u=0):
    """ Esta función calcula el valor de hacer n clicks en aun anuncio tipo
    naranja de neobux hecho por un referido.
    n es un valor entero y es la cantidad de clicks
    tipo_r es un valor INT del referido vale 0 si es directo y != 0 si es alquilado
    tipo_u es un valor INT del usuraio vale 1 si es gold !=0 si es standar
    """
    if (tipo_u==0): #Usuario standar
        if (tipo_r==0):
            click = 0.0005
        else:
            click = 0.0050
    else: #Usuario gold
        if (tipo_r==0):
            click = 0.0050
        else:
            click = 0.0100
    return n * click

            

