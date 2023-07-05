import pygame
from BB_Modificacion_imagenes import *
from CC_Pantalla import *

# MOVIMIENTOS:
# 
personaje_quieto_izquierda = [pygame.image.load("Fotos\Parada.png")]
# 
personaje_quieto_derecha = girar_imagenes(personaje_quieto_izquierda, True, False)

personaje_camina_izquierda = [pygame.image.load("E:\KITTY\Movimientos_kitty\Camino_1.png"),
                    pygame.image.load("E:\KITTY\Movimientos_kitty\Movimientos_3.png"),
                    pygame.image.load("E:\KITTY\Movimientos_kitty\Camino_2.png"),
                    pygame.image.load("E:\KITTY\Movimientos_kitty\Movimientos_3.png")]

personaje_camina_derecha = girar_imagenes(personaje_camina_izquierda, True, False)

personaje_salta_izquierda = [pygame.image.load("E:\KITTY\Movimientos_kitty\Saltando.png")]
personaje_salta_derecha = girar_imagenes(personaje_salta_izquierda, True, False)


# ATAQUES:
personaje_ataque_principal = [pygame.image.load("E:\KITTY\Movimientos_kitty\Camino_1.png")]

personaje_ataque_secundario = [pygame.image.load("E:\KITTY\Movimientos_kitty\Camino_1.png")]

# MUERTE:
personaje_muerte_izquierda = [pygame.image.load("Muerte\Muerte_uno.png"),
                            pygame.image.load("Muerte\Muerte_dos.png"),
                            pygame.image.load("Muerte\Muerte_tres.png")]

personaje_muerte_derecha = girar_imagenes(personaje_muerte_izquierda, True, False)

# posiciones, tamaños
posicion_inicial = (H / 2 - 300, 650)
tamaño = (75, 85)


# diccionario acciones
diccionario_animaciones = {}
diccionario_animaciones["quieto_derecha"] = personaje_quieto_derecha
diccionario_animaciones["quieto_izquierda"] = personaje_quieto_izquierda
diccionario_animaciones["salta_izquierda"] = personaje_salta_izquierda
diccionario_animaciones["salta_derecha"] = personaje_salta_derecha
diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda
diccionario_animaciones["camina_derecha"] = personaje_camina_derecha
diccionario_animaciones["Muerte_derecha"] = personaje_muerte_derecha
diccionario_animaciones["Muerte_izquierda"] = personaje_muerte_izquierda

diccionario_animaciones["frutilla"] = personaje_ataque_principal
diccionario_animaciones["monio"] = personaje_ataque_secundario