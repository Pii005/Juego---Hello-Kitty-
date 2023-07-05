import pygame
from CC_Pantalla import *
from PIL import Image

pygame.font.init()
color_blanco = (255, 255, 255)

def crear_texto(pantalla, texto, posicion, color, tamaño):
    Formato = pygame.font.Font(None, tamaño)
    texto = Formato.render(texto, True, color)
    pantalla.blit(texto, posicion)


def mostrar_vidas(cantidad_vidas):
    if cantidad_vidas <= 0:
        imagen_path = "imagen_game_over.jpg"  # Ruta de la imagen para 0 vidas o menos
    elif cantidad_vidas == 1:
        imagen_path = "imagen_vida_1.jpg"  # Ruta de la imagen para 1 vida
    elif cantidad_vidas == 2:
        imagen_path = "imagen_vida_2.jpg"  # Ruta de la imagen para 2 vidas
    else:
        imagen_path = "imagen_vida_default.jpg"  # Ruta de la imagen por defecto para más de 2 vidas

    # Cargar y mostrar la imagen
    imagen = Image.open(imagen_path)
    imagen.show()



# frutillas = Crear_texto(pantalla, "Frutillas: ", (100, 100), color_blanco, 20)

# listas_textos = [frutillas]