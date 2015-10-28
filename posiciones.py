# archivo que tiene funciones para pintar la posicion de un robot

car_rep_primero = "-"
car_rep_ultimo = "-"
car_rep_relleno = " "
car_rep_posicion = "*"

def pinta_simple (maximo_x, caracter):
    print ("|%s|" % (caracter * (maximo_x - 2)))

def pinta_primero (maximo_x):
    pinta_simple (maximo_x, car_rep_primero)

def pinta_ultimo (maximo_x):
    pinta_simple (maximo_x, car_rep_ultimo)

def pinta_relleno (maximo_x):
    pinta_simple (maximo_x, car_rep_relleno)

def pinta_posicion (maximo_x, caracter, posicion, caracter_pos):
    if posicion == 0:
        print ("%s%s|" % (caracter_pos, caracter * (maximo_x - 2)))
    elif posicion == maximo_x - 1:
        print ("|%s%s" % (caracter * (maximo_x - 2), caracter_pos))
    else:
        print ("|%s%s%s|" % (caracter * (posicion - 1), caracter_pos,
                             caracter * (maximo_x - posicion - 2)))

def pinta_malla (x, y, maximo_x, maximo_y):
    # el contador va al reves
    for i in range (maximo_y-1, -1, -1):
        # se verifica si se tiene que dibujar la posicion del robot o no
        if i == y:
            if i == 0 or i == maximo_x - 1:
                pinta_posicion (maximo_x, "-", x, "*")
            else:
                pinta_posicion (maximo_x, " ", x, "*")
        else:
            if i == 0:
                pinta_primero (maximo_x)
            elif i == maximo_x - 1:
                pinta_ultimo (maximo_x)
            else:
                pinta_simple (maximo_x, " ")


