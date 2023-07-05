from typing import Any
import pygame
# from pygame.sprite import _Group, Sprite
from BB_Modificacion_imagenes import *
# from AA_Kitty import Personaje
from CC_Archivos_ataques import *
from CC_textos import *
from CC_Pantalla import *


# class proyectil():
#     def __init__(self, animacion) -> None:
#         self.reescalar = reescalar_imagenes(animacion, 40, 40)
#         self.animaciones = animacion
#         self.rectangulo_proyectil = self.animaciones[0].get_rect()
#         self.rectangulo_proyectil_lados = obtener_rectangulo(self.rectangulo_proyectil)
#         # self.posicion = ubicacion_personaje
#         # self.posicion.x = ubicacion_personaje[0]
#         # self.posicion.y = ubicacion_personaje[1]
#         self.rectangulo_proyectil.x = 800
#         self.rectangulo_proyectil.y = 400
#         self.rectangulo.center = (self.rectangulo_proyectil.x, self.rectangulo_proyectil.y)
        

#     def mover(self, velocidad):
#         for lado in self.lados:
#             self.lados[lado].x += velocidad

#     def update(self):
#         pass

    # def crear_proyectil(self, pantalla):
    #     pantalla.blit(self.animaciones[0], self.lados_proyectil["main"])
    #     print("Entro")



# rectangulo = self.animaciones["camina_derecha"][0].get_rect()
#         rectangulo.x = posicion_inicial[0]
#         rectangulo.y = posicion_inicial[1]

# para la parte de direccion obtendra un Booleano
# donde si es True es izquierda y si es False es derecha

# 

# self.reescalar = reescalar_imagenes(animacion, 40, 40)
#         self.animaciones = animacion
#         self.rectangulo_frutilla = self.animaciones[0].get_rect()
        
#         self.rectangulo_frutilla.x = posiciones[0]
#         self.rectangulo_frutilla.y = posiciones[1]
#         self.lados_frutilla = obtener_rectangulo(self.rectangulo_frutilla)
#         self.elemento = elemento
#         self.contador_llaves = 0
#         self.contador_frutillas = 0



# class Proyectil:
#     def __init__(self, ubicacion, animacion):
#         self.animaciones = reescalar_imagenes(self.animaciones, 20, 20)
#         self.animaciones = animacion
#         self.rectangulo = self.animaciones[0].get_rect()
#         self.lados = obtener_rectangulo(self.rectangulo)

#         self.rectangulo.center = ubicacion

#     def mover(self, velocidad):
#         for lado in self.lados:
#             self.lados[lado].x += velocidad
            
#     def update(self, movimiento):
#         if movimiento == "Izquierda":
#             self.mover(10)
#         else:
#             self.mover(-10)

''' YO '''
# class Proyectiles():
#     def __init__(self, x, y) -> None:
#         self.animaciones = diccionario_ataques
#         self.reescalar_animaciones()
#         self.rectangulo_frutilla = self.animaciones["Frutilla"][0].get_rect()
#         self.lados = obtener_rectangulo(self.rectangulo_frutilla)
#         self.rectangulo_frutilla.x = x
#         self.rectangulo_frutilla.y = y#Centro de la imagen
#         self.contador_pasos = 0
        

#     def mover(self, velocidad):
#         for lado in self.lados:
#             self.lados[lado].x += velocidad

#     def animar(self, pantalla, que_animacion):
#         animacion = self.animaciones[que_animacion]
#         largo = len(animacion)
        
#         if self.contador_pasos >= largo:
#             self.contador_pasos = 0
        
#         pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
#         self.contador_pasos += 1

#     def reescalar_animaciones(self):
#         for clave in self.animaciones:
#             reescalar_imagenes(self.animaciones[clave], 40, 40)

#     def update(self, pantalla):
#         self.mover(10)
#         self.animar(pantalla, "Frutilla")

#         pantalla.blit(self.animaciones[0], self.rectangulo_frutilla)
#         if self.rectangulo.bottom < 0:
#             self.kill() #elimina si pasa los bordes 
        


''' VIDEO '''
# class Tiro(pygame.sprite.Sprite):
#     def __init__(self, x, y) -> None:
#         super().__init__()
#         self.image = pygame.transform.scale(pygame.image.load("Ataques\Sin Fondo_Frutilla.png").convert(), (40,40))
#         self.image.set_colorkey("Black")
#         self.rect = self.image.get_rect()
#         self.rect.bottom = y 
#         self.rect.centerx = x
    
#     def update(self) -> None:
#         self.rect.x -= 30
#         if self.rect.bottom < 0:
#             self.kill

# bala = pygame.sprite.Group()


''' Otro'''
# class Proyectil:
#     def __init__(self, x, y, direccion):
#         self.x = x
#         self.y = y
#         self.direccion = direccion
#         self.velocidad = 5
#         self.imagen = pygame.image.load("proyectil.png")
#         self.rectangulo = self.imagen.get_rect()
#         self.rectangulo.center = (self.x, self.y)

#     def update(self, pantalla):
#         self.x += self.velocidad * self.direccion
#         self.rectangulo.center = (self.x, self.y)
#         pantalla.blit(self.imagen, self.rectangulo)


# class Bullet(Sprite):
#     def __init__(self, a_game) -> None:
#         super().__init__()
#         self.screen = a_game.screen
#         self.color = a_game.colorbala
#         self.rect = pygame.Rect(0,0, a_game.anchobala, a_game.altobala)


# class Proyectil:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.velocidad = 5

#     def actualizar(self):
#         self.y -= self.velocidad
    
#     def dibujar(self):
#         pygame.draw.circle(pantalla, "Red", (self.x, self.y), 5)

#     def update(self):
#         self.actualizar()
#         self.dibujar()

# lista_proyectil = []

class Proyectil:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 5

    def update(self):
        self.y -= self.velocidad

    def draw(self, pantalla):
        pygame.draw.circle(pantalla, (255, 0, 0), (self.x, self.y), 5)  # Dibuja un círculo rojo como proyectil