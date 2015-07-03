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

def ganancia (tipo_usuario, anuncios_n, anuncios_m, media_rd, media_ra, referidos_a, referidos_d , costo_ra):
    
    ganado_u = (a_morado(anuncios_m,tipo_usuario) + a_naranja (anuncios_n,tipo_usuario))*30 #ganado en un mes por el usuario
    click_rd = media_rd * 30
    ganado_rd =  r_a_naranja (click_rd,0,tipo_usuario)  * referidos_d
    click_ra = media_ra * 30
    ganado_ra =  r_a_naranja (click_ra,1,tipo_usuario)  * referidos_a

    total_ganado = ganado_u + ganado_rd + ganado_ra
    total_ganado = total_ganado - costo_ra * referidos_a
    return round(total_ganado,3)

def mostrar_ganancia (tipo_usuario, anuncios_n, anuncios_m, media_rd, media_ra, referidos_a, referidos_d , costo_ra):

    if (tipo_usuario == 0):
        txt = 'standar'
    else:
        txt = 'gold'
    print ("Para un usuario",txt,"con",referidos_d,"referidos directos y",referidos_a,"referidos alquilados")
    ganado = ganancia (tipo_usuario, anuncios_n, anuncios_m, media_rd, media_ra, referidos_a, referidos_d , costo_ra)
    print ("podemos estimar que ganara minimo",ganado,"$ al mes")
    

##deja estas lineas asi comentadas como esta luego las usaremos
    
##tipo_usuario = 0 # 0 standar 1 gold
##anuncios_n = 4 # anuncios validos naranja para el usuario
##anuncios_m = 19 # anuncios micro y morados del usuario
##media_rd = 2 # media del referido directo
##media_ra = 1.6 # media del referido alquilado
##referidos_d = 1 # referidos directo
##referidos_a = 3# referidos alquilados
##costo_ra = 0.25 # referido alquilado mensual


tipo_usuario = int(input ('cuál es tu tipo de usuario (0 o 1)? '))
anuncios_n = int( input ('cuantos anuncios validos naranjas usted ve diario: '))  
referidos_d = int(input('cauntos referidos directos posee usted en su cuanta '))
referidos_a = int(input('cauntos referidos  alquilados posee usted en su cuanta '))
media_rd = int(input('cual es la media del los referido directo que usted posee'))
media_ra = int(input('cual es la media del los referido alquilado que usted posee'))
costo_ra = int(input('cuanto es el costo mensual todos de sus referido alquilados '))

mostrar_ganancia (tipo_usuario, anuncios_n, anuncios_m, media_rd, media_ra, referidos_a, referidos_d , costo_ra)
