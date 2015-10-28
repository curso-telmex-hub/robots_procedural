from unittest import TestCase
import movs_robots as movsr
import posiciones as pos

# test para probar los movimientos de un robot en una malla
class movimientos_tests(TestCase):
    """supone que las posiciones de las x's y y's son mayores iguales  a cero"""
    def test_movimientos_simples(self):
        pos_x = 10
        pos_y = 15

        # se prueba la funcion a la derecha
        self.assertEqual(movsr.derecha (pos_x), 11)

        # se prueba la funcion a la izquierda
        self.assertEqual(movsr.izquierda (pos_x), 9)

        # se prueba la funcion a la arriba
        self.assertEqual(movsr.arriba (pos_y), 16)

        # se prueba la funcion a la abajo
        self.assertEqual(movsr.abajo (pos_y), 14)

    def test_movimientos_acotados (self):
        pos_x = 10
        max_x_1 = pos_x
        max_x_2 = pos_x + 1
        min_x_1 = pos_x
        min_x_2 = pos_x - 1

        pos_y = 15
        max_y_1 = pos_y
        max_y_2 = pos_y + 1
        min_y_1 = pos_y
        min_y_2 = pos_y - 1

        # se prueba la funcion a la derecha
        # no se puede mover
        self.assertEqual(movsr.derecha_m (pos_x, max_x_1), pos_x)
        # si se puede mover
        self.assertEqual(movsr.derecha_m (pos_x, max_x_2), pos_x + 1)

        # se prueba la funcion a la izquierda
        # no se puede mover
        self.assertEqual(movsr.izquierda_m (pos_x, min_x_1), pos_x)
        # si se puede mover
        self.assertEqual(movsr.izquierda_m (pos_x, min_x_2), pos_x - 1)

        # se prueba la funcion a la arriba
        # no se puede mover
        self.assertEqual(movsr.arriba_m (pos_y, max_y_1), pos_y)
        # si se puede mover
        self.assertEqual(movsr.arriba_m (pos_y, max_y_2), pos_y + 1)

        # se prueba la funcion a la abajo
        # no se puede mover
        self.assertEqual(movsr.abajo_m (pos_y, min_y_1), pos_y)
        # si se puede mover
        self.assertEqual(movsr.abajo_m (pos_y, min_y_2), pos_y - 1)

    def test_posiciones (self):
        """ se verifica que se pinten bien la posicion del robot"""
        # las posiciones van de 0 a n-1
        x, y = (2, 0)
        max_x, max_y = (10,10)
        print ("x = %d, y = %d, max_x = %d, max_y = %d" % (x, y, max_x, max_y))
        pos.pinta_posicion (max_x, "-", 0, "*")
        pos.pinta_posicion (max_x, "-", 9, "*")
        pos.pinta_posicion (max_x, "-", 1, "*")
        pos.pinta_posicion (max_x, "-", 2, "*")
        pos.pinta_posicion (max_x, "-", 3, "*")
        pos.pinta_posicion (max_x, "-", 4, "*")
        pos.pinta_posicion (max_x, "-", 8, "*")

    def test_malla (self):
        """se prueba la malla"""
        # las posiciones van de 0 a n-1
        x, y = (3, 10)
        max_x, max_y = (20, 20)
        print ("x = %d, y = %d, max_x = %d, max_y = %d" % (x, y, max_x, max_y))
        pos.pinta_malla (x, y, max_x, max_y)
