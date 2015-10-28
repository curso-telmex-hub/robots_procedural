# archivo con las funciones que mueven a un robot

# mueve el robot a la derecha una unidad
def derecha (x):
    return x+1 

# mueve el robot a la izquierda una unidad
def izquierda (x):
    return x-1

# mueve el robot arriba una unidad
def arriba (y):
    return y + 1

# mueve el robot para abajo una unidad
def abajo (y):
    return y - 1


# mueve el robot a la derecha una unidad y
# verifica que no se puede salir de la maya
def derecha_m (x, x_max):
    if x < x_max:
        # se reusa el codigo realizado
        return derecha (x)
    else:
        return x

# mueve el robot a la izquierda una unidad
def izquierda_m (x, x_min):
    if x > x_min:
        # se reusa el codigo realizado
        return izquierda (x)
    else:
        return x

# mueve el robot arriba una unidad
def arriba_m (y, y_max):
    if y < y_max:
        # se reusa el codigo realizado
        return arriba (y)
    else:
        return y

# mueve el robot para abajo una unidad
def abajo_m (y, y_min):
    if y > y_min:
        # se reusa el codigo realizado
        return abajo (y)
    else:
        return y


    
