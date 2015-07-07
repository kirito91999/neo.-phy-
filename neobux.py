def a_morado (n=1,tipo=0):
    """ (int,int)-> float 

    Esta función calcula el valor de hacer n clicks en aun anuncio tipo
    morado o gris (micro) de neobux.
    n es un valor entero y es la cantidad de clicks
    tipo es un valor INT vale 1 si es gold 0 si es standar

    >>>a_morado()
    0.001
    >>>a_morado(5)
    0.005
    >>>a_morado(0)
    0.0
    >>>a_morado(0,0)
    0.0
    >>>a_morado(5,0)
    0.005
    >>>a_morado(0,1)
    0.0
    >>>a_morado(5,1)
    0.005
    """
    if (tipo==0):
        click = 0.001
    else:
        click = 0.001
    return n * click

def a_naranja (n=1,tipo=0):
    """ (int,int) -> float

    Esta función calcula el valor de hacer n clicks en aun anuncio tipo
    naranja de neobux.
    n es un valor entero y es la cantidad de clicks
    tipo es un valor INT vale 1 si es gold 0 si es standar

    >>>a_naranja()
    0.001
    >>>a_naranja(5,1)
    0.010
    >>>a_naranja(5,0)
    0.001
    >>>a_naranja(0,1)   
    0.0
    >>>a_naranja(0,0)
    o.o
    """
    if (tipo==0):
        click = 0.001
    else:
        click = 0.010
    return n * click

def r_a_naranja (n=1,tipo_r=0,tipo_u=0):
    """(int,int,int) ->  float

    Esta función calcula el valor de hacer n clicks en sun anuncio tipo
    naranja de neobux hecho por un referido.
    n es un valor entero y es la cantidad de clicks
    tipo_r es un valor INT del referido vale 0 si es directo y 1 si es alquilado
    tipo_u es un valor INT del usuraio vale 1 si es gold o 0 si es standar

    >>>r_a_naranja (0,0)
    0.0
    >>>r_a_naranja()
    0.0005
    >>>r_a_naranja(1,1)
    0.005
    >>>r_a_naranja(0,0)
    0.0
    >>>r_a_naranja(0,0,1)
    0.0
    >>>r_a_naranja(1,0,1)
    0.005
    >>>r_a_naranja(1,1,1)
    0.01
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
    '''(int, int, int, float, float, int, int, float) -> float 

    esta funcion calcula de su ganancia total de un mes de trabajo en neobux.
    tomando en cuenta:
    tipo_usuario es un valor INT vale 1 si es gold 0 si es standar
    anuncios_n es un INT que indica la cantidad de anuncios naranjas vistos por ud.
    anuncios_m es un INT que indica la cantidad de anuncios morados y/o micros vistos por ud.
    media_rd, media_ra son valores float que indican la media de los referidos directo y referidos alquilados respectivamente
    referidos_d, referidos_a  son valores INT que corresponden a los referidos directo y referidos alquilados respectivamente
    costo_ra costo de los referidos alquilados en float.
    

    >>>ganancia(0,0,0,1.0,1.0,0,0,1.0)
    0.0
    >>>ganancia(1,5,5,1.7,1.7,5,5,1.7)
    -3.025
    

   ''' 
    ganado_u = (a_morado(anuncios_m,tipo_usuario) + a_naranja (anuncios_n,tipo_usuario))*30 #ganado en un mes por el usuario
    click_rd = media_rd * 30
    ganado_rd =  r_a_naranja (click_rd,0,tipo_usuario)  * referidos_d
    click_ra = media_ra * 30
    ganado_ra =  r_a_naranja (click_ra,1,tipo_usuario)  * referidos_a

    total_ganado = ganado_u + ganado_rd + ganado_ra
    total_ganado = total_ganado - costo_ra * referidos_a
    return round(total_ganado,3)

def mostrar_ganancia (tipo_usuario, anuncios_n, anuncios_m, media_rd, media_ra, referidos_a, referidos_d , costo_ra):
    '''(int,int,int,float,float,int,int,float) -> str

    tipo_usuario es un valor INT vale 1 si es gold 0 si es standar
    anuncios_n es un INT que indica la cantidad de anuncios naranjas vistos por ud.
    anuncios_m es un INT que indica la cantidad de anuncios morados y/o micros vistos por ud.
    media_rd, media_ra son valores float que indican la media de los referidos directo y referidos alquilados respectivamente
    referidos_d, referidos_a  son valores INT que corresponden a los referidos directo y referidos alquilados respectivamente
    costo_ra costo de los referidos alquilados en float.

    >>>mostrar_ganancia (0,0,0,1.0,1.0,0,0,1.0)
    Para un usuario standar con 0 referidos directos y 0 referidos alquilados
    podemos estimar que ganara minimo 0.0 $ al mes. 

    Gracias por elegir nuestro programa de jluna80 y kirito91999  para calcualr sus ganancias. es 100% gratis XD XD
    >>>mostrar_ganancia (1,5,5,1.7,1.7,5,5,1.7)
    Para un usuario gold con 5 referidos directos y 5 referidos alquilados
    podemos estimar que ganara minimo -3.025 $ al mes. 
    
    Gracias por elegir nuestro programa de jluna80 y kirito91999  para calcualr sus ganancias. es 100% gratis XD XD
    >>>mostrar_ganancia (1,5,5,1.7,1.7,5,5,0.2)
    Para un usuario gold con 5 referidos directos y 5 referidos alquilados
    podemos estimar que ganara minimo 4.475 $ al mes. 

    Gracias por elegir nuestro programa de jluna80 y kirito91999  para calcualr sus ganancias. es 100% gratis XD XD
    
    '''
    if (tipo_usuario == 0):
        txt = 'standar'
    else:
        txt = 'gold'
    print ("Para un usuario",txt,"con",referidos_d,"referidos directos y",referidos_a,"referidos alquilados")
    ganado = ganancia (tipo_usuario, anuncios_n, anuncios_m, media_rd, media_ra, referidos_a, referidos_d , costo_ra)
    print ("podemos estimar que ganara minimo",ganado,"$ al mes. \n\nGracias por elegir nuestro programa de jluna80 y kirito91999  para calcualr sus ganancias. es 100% gratis XD XD")
    

##deja estas lineas asi comentadas como esta luego las usaremos
    
##tipo_usuario = 0 # 0 standar 1 gold
##anuncios_n = 4 # anuncios validos naranja para el usuario
##anuncios_m = 19 # anuncios micro y morados del usuario
##media_rd = 2 # media del referido directo
##media_ra = 1.6 # media del referido alquilado
##referidos_d = 1 # referidos directo
##referidos_a = 3# referidos alquilados
##costo_ra = 0.25 # referido alquilado mensual


import os
continuar = True

while (continuar):
    print ('Calculo estimado de utilidad en Neobux\n')
    tipo_usuario = int(input ('cuál es tu tipo de usuario (0 para standar  o 1 para gold)?: '))
    anuncios_n = int( input ('cuantos anuncios validos naranjas usted ve diario (4 recomendado): '))
    anuncios_m = int(input('cuantos anuncios validos morados o micro usted ve diario: '))
    referidos_d = int(input('cauntos referidos directos posee usted en su cuenta: '))
    media_rd = 0
    media_ra = 0
    costo_ra = 0
    if (referidos_d > 0):
        media_rd = float(input('cual es la media del los referidos directos que usted posee: '))
    referidos_a = int(input('cauntos referidos  alquilados posee usted en su cuenta: '))
    if (referidos_a > 0):
        media_ra = float(input('cual es la media del los referidos alquilados que usted posee: '))
        costo_ra = float(input('cuanto es el costo mensual de cada uno de sus referidos alquilados: '))
    print ('\n')
    mostrar_ganancia (tipo_usuario, anuncios_n, anuncios_m, media_rd, media_ra, referidos_a, referidos_d , costo_ra)
    res=input('\nDesea volver a probar con otros datos (S/N): ').upper()
    if (res == 'N'):
        continuar = False
    os.system('cls')
