import pygame
from BB_Modificacion_imagenes import *
# from AA_Kitty import Personaje
from CC_Archivos_ataques import *
from CC_textos import *

class Elementos ():
    def __init__(self, animacion, posiciones) -> None:
        self.reescalar = reescalar_imagenes(animacion, 40, 40)
        self.animaciones = animacion
        self.rectangulo_elemento = self.animaciones[0].get_rect()
        self.rectangulo_elemento.x = posiciones[0]
        self.rectangulo_elemento.y = posiciones[1]
        self.lados = obtener_rectangulo(self.rectangulo_elemento)

    def update(self, pantalla):
        pantalla.blit(self.animaciones[0], self.rectangulo_elemento)

    def puntajes(self, pantalla):
        crear_texto(pantalla, f"Frutillas: {self.contador_frutillas}", (200,10), (255, 255, 255), 20)


frutilla_uno = Elementos(animaciones_frutilla, (309, 581))

frutilla_dos = Elementos(animaciones_frutilla, (414, 582))
frutilla_tres = Elementos(animaciones_frutilla, (542, 585))

frutilla_cuatro = Elementos(animaciones_frutilla, (652, 464))
frutilla_cinco = Elementos(animaciones_frutilla, (765, 462))
frutilla_seis = Elementos(animaciones_frutilla, (879, 463))

frutilla_siete = Elementos(animaciones_frutilla, (1071, 363))
frutilla_ocho = Elementos(animaciones_frutilla, (1190, 359))
frutilla_nueve = Elementos(animaciones_frutilla,(546, 243))

frutilla_diez = Elementos(animaciones_frutilla,(657, 244))
frutilla_once = Elementos(animaciones_frutilla,(838, 244))


lista_objetos = [frutilla_uno, frutilla_dos, frutilla_tres, frutilla_cuatro, frutilla_cinco, 
                frutilla_seis, frutilla_siete, frutilla_ocho, frutilla_nueve,frutilla_diez,
                frutilla_once]

elemento_recuperar_uno = Elementos(animacion_mas_vidas, (1328, 364))

lista_recuperar = [elemento_recuperar_uno]
