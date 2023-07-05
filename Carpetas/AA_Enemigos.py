
import pygame
from AA_archivos_enemigo import *
from BB_Modificacion_imagenes import *
from AA_Kitty import *
import random


class enemigo():
    def __init__(self, inicio, final, animaciones, tamaño):
        self.vidas = 1
        self.ancho = tamaño [0]
        self.alto = tamaño [1]
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        # self.esta_saltando = False
        self.desplazamiento_y = 0
        # animacion:
        self.contador_pasos = 0
        self.acciones = "Movimiento_derecha"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        # Hitbot
        rectangulo = self.animaciones["Movimiento_derecha"][0].get_rect()
        rectangulo.x = inicio[0]
        rectangulo.y = inicio[1]
        self.lados = obtener_rectangulo(rectangulo)
        self.velocidad = 5
        self.movimiento_inicio = inicio
        self.movimiento_final = final  
        self.direccion = 1   

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], self.ancho, self.alto)
    
    def animar(self, pantalla, que_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1
    
    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad
    
    def update(self, pantalla, lista_plataformas):
        if self.direccion == 1:
            if self.lados["main"].x < self.movimiento_final[0]:
                self.animar(pantalla, "Movimiento_derecha")
                self.mover(self.velocidad)
            else:
                self.animar(pantalla, "Movimiento_derecha")
                self.direccion = -1  
        else:
            if self.lados["main"].x > self.movimiento_inicio[0]:
                self.animar(pantalla, "Movimiento_derecha")
                self.mover(-self.velocidad)  
            else:
                self.animar(pantalla, "Movimiento_derecha")
                self.direccion = 1 
        self.aplicar_gravedad(lista_plataformas)

    def aplicar_gravedad(self, lista_plataformas):
        for lado in self.lados:
            self.lados[lado].y += self.desplazamiento_y
        if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
            self.desplazamiento_y += self.gravedad

        # for lados in lista_plataformas:
        #     if self.lados["bottom"].colliderect(lados["top"]):
        #         self.lados["main"].bottom = lados["main"].top + 5
        #         self.desplazamiento_y = 0
        #         self.esta_saltando = False
        for plataforma in lista_plataformas:
            if self.lados["bottom"].colliderect(plataforma):
                self.lados["main"].bottom = plataforma.top + 5
                self.desplazamiento_y = 0
                self.esta_saltando = False


# (1019, 618)
# (1090, 650)

Humberto = enemigo((284, 545),(597, 557),diccionario_enemigo, Tamaño_enemigo)
enemigo_dos = enemigo((525, 202), (819, 200), diccionario_enemigo, Tamaño_enemigo)
enemigo_tres = enemigo((706, 657), (1265, 654), diccionario_enemigo, Tamaño_enemigo)

Enemigos = [Humberto, enemigo_dos, enemigo_tres]












'''
ELIMINACION DE ENEMIGO AL SER GOLPEADO:
Define una función que verifique si hay una colisión entre el cuadrado y el otro objeto. 
Puedes utilizar el método colliderect() de los rectángulos para verificar si se superponen.
python

def verificar_colision(cuadrado, otro_objeto):
    if cuadrado.colliderect(otro_objeto):
        return True
    else:
        return False

Dentro de tu bucle principal de juego, donde se actualiza la lógica y se dibujan los objetos en la pantalla, 
verifica si hay una colisión entre el cuadrado y el otro objeto utilizando la función que acabamos de definir.
python

if verificar_colision(cuadrado, otro_objeto):
# Se produce una colisión, elimina el cuadrado
cuadrado = None

Si se produce la colisión y deseas eliminar el cuadrado de forma permanente, puedes asignarle el valor None. 
Esto indica que ya no se está utilizando y será eliminado por el recolector de basura de Python.
Al asignar cuadrado = None, el cuadrado ya no se dibujará ni se actualizará en el siguiente ciclo del bucle principal, 
y se eliminará automáticamente de la memoria.



'''