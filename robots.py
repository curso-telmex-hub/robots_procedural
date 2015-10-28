"""programa que va pintando el movimiento de un robot"""
import random
import movs_robots as movsr
import posiciones as pos

# se inicializa aleatoriamente la posicion de un robot
max_x = 10
max_y = 10
x = random.randint (0, max_x - 1)
y = random.randint (0, max_y - 1)

# va pintando la posicion de un robot, sale del ciclo con la letra q
print ("Sale del ciclo con la letra 'q'")
while True:
    pos.pinta_malla (x, y, max_x, max_y)
    cadena = str (input (">>> "))
    if cadena == "q":
        break
    else:
        # se obtiene el siguiente moviento
        n_movs = 20              # numero de movimientos
        mov_hor = random.randint (1, n_movs)
        
        print ("x = %d, y = %d" % (x, y))
        if mov_hor % 2 == 0:
            print ("derecha")
            x = movsr.derecha_m (x, max_x - 1)
        else:
            print ("izquierda")
            x = movsr.izquierda_m (x, 0)
        print ()
    
        mov_vert = random.randint (1, n_movs)
        if mov_vert % 2 == 0:
            print ("arriba")
            y = movsr.arriba_m (y, max_y - 1)
        else:
            print ("abajo")
            y = movsr.abajo_m (y, 0)
        print ("x = %d, y = %d" % ( x, y))
