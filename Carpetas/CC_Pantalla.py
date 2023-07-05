import pygame
import time
from CC_textos import *

W, H = 1500, 900
TAMAÑO_PANTALLA = (W, H)
FPS = 20

RELOJ = pygame.time.Clock()
pantalla = pygame.display.set_mode(TAMAÑO_PANTALLA)


pygame.display.set_caption("Hello Kitty Adventure")
icono = pygame.image.load("Fotos\Logo.png")
pygame.display.set_icon(icono)

# Fondo
fondo = pygame.image.load("Fotos\Fondo_practico.png")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)


lista_colores = ["Red", "Yellow", "Black", "White",
                "Green", "Orange", "Pink", "Purple",
                "Brown","Cyan","Gray", "Magenta"]

def contador_reloj(tiempo_inicial, pantalla):
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial
    minutos = tiempo_transcurrido // 60000
    segundos = (tiempo_transcurrido // 1000) % 60

    crear_texto(pantalla, f"{minutos:02d}:{segundos:02d}", (1402, 16), (255, 255, 255), 24)

tiempo_inicial = pygame.time.get_ticks()

