
import pygame
from AA_archivos_kitty import *
from BB_Modificacion_imagenes import *
from CC_Recolectar import *
from CC_Archivos_ataques import *
from CC_textos import *
from AA_proyectiles import *
from CC_Archivos_ataques import *
from CC_Pantalla import *

import pygame.sprite

# lista_proyectiles = []

# recolectar_frutillas = pygame.mixer.Sound("")

class Personaje():
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad):
        self.vidas = 3
        # Configuración
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        # Gravedad
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        self.desplazamiento_y = 0
        # Animaciones
        self.contador_pasos = 0
        self.que_hace = diccionario_animaciones["quieto_derecha"]
        self.animaciones = animaciones
        self.reescalar_animaciones()
        # Rectángulos
        self.rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)
        self.velocidad = velocidad
        # Movimientos:
        self.bandera_derecha = True
        self.bandera_izquierda = False
        # daños:
        self.tiempo_invulnerable = 0
        self.tiempo_invulnerable_total = 1 * 60

        self.bandera_gravedad = True
        self.posicion_inicial = posicion_inicial

        #PUNTOS:
        self.contador_llaves = 0
        self.contador_frutillas = 0

        self.lista_proyectil = []
    
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
    
    def aplicar_gravedad(self, pantalla, lista_plataformas):
            if self.esta_saltando:
                if self.bandera_derecha == True:
                    self.animar(pantalla, "salta_derecha")
                elif self.bandera_izquierda == True:
                    self.animar(pantalla, "salta_izquierda")
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        
            for plataforma in lista_plataformas:
                if self.lados["bottom"].colliderect(plataforma):
                    self.lados["main"].bottom = plataforma.top + 5
                    self.desplazamiento_y = 0
                    self.esta_saltando = False


    def update(self, pantalla, lista_plataformas, lista_enemigos, lista_objetos, lista_mas_vidas, trampas):
        if self.que_hace == "derecha":
            nueva_x = self.rectangulo.x + 10
            if nueva_x < W - self.rectangulo.width:
                self.mover(self.velocidad)
            if not self.esta_saltando:
                self.animar(pantalla, "camina_derecha")
            self.bandera_derecha = True
            self.bandera_izquierda = False

        elif self.que_hace == "izquierda":
            nueva_x = self.rectangulo.x - 10
            if nueva_x > 0:
                self.mover(-self.velocidad)
            if not self.esta_saltando:
                self.animar(pantalla, "camina_izquierda")
            self.bandera_derecha = False
            self.bandera_izquierda = True    
            
        elif self.que_hace == "salta":
            if self.bandera_derecha == True:
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            elif self.bandera_izquierda == True:
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
        elif self.que_hace == "quieto":
            if self.bandera_derecha == True:
                if not self.esta_saltando:
                    self.animar(pantalla, "quieto_derecha")
            elif self.bandera_izquierda == True:
                if not self.esta_saltando:
                    self.animar(pantalla, "quieto_izquierda")
        # if self.que_hace == "Ataque_Frutilla":
        #     self.animar(pantalla, "frutilla")
        #     self.disparar()

        ### DAÑOS ###
        if self.vidas == 0:
            # print("El juegador a muerto")
            self.restablecer_personaje()
            self.bandera_gravedad = True

        self.trampas(pantalla, trampas)
        self.daño_enemigos(pantalla, lista_enemigos)
        if self.tiempo_invulnerable > 0:
            self.tiempo_invulnerable -= 1
        
        ### Puntos ###
        self.puntos(pantalla, lista_objetos)
        self.obtener_vidas(pantalla, lista_mas_vidas)

        self.aplicar_gravedad(pantalla, lista_plataformas)

    # def ataques(self, pantalla):
    #     # ff = Tiro(self.rectangulo.centerx, self.rectangulo.top + 50)
    #     # bala.add(ff)
    #     # bala.update()
    #     disparo = Proyectiles(self.lados["main"].x, self.lados["main"].y)
    #     lista_proyectiles.append(disparo)

    # def disparar(self):
    #     # proyectil = Proyectil(self.rectangulo.centerx, self.rectangulo.top + 50)
    #     # lista_proyectil.append(proyectil)
    #     proyectil = Proyectil(self.rectangulo.centerx, self.rectangulo.top + 50)
    #     self.lista_proyectil.append(proyectil)


    

    def daño_enemigos(self, pantalla, lista_enemigos):
        if self.tiempo_invulnerable == 0:  
            for enemigo in lista_enemigos:
                if self.lados["main"].colliderect(enemigo.lados["main"]):
                    self.vidas -= 1
                    self.sonido_vidas = pygame.mixer.Sound("musica\Menos_vida.wav")
                    self.sonido_vidas.play()
                    self.tiempo_invulnerable = self.tiempo_invulnerable_total
                    break
        self.datos(pantalla)

    def puntos(self, pantalla, lista_elemento):
        for elemento in lista_elemento:
            if self.lados["main"].colliderect(elemento.lados["main"]):
                self.contador_frutillas += 1
                self.sonido = pygame.mixer.Sound("musica\Frutila.wav")
                self.sonido.play()
                lista_elemento.remove(elemento)
            else:
                elemento.update(pantalla)
        self.datos(pantalla)
    
    
    def llaves(self):
        pass

    def obtener_vidas(self,pantalla, lista_elementos):
        for elemento in lista_elementos:
            if self.lados["main"].colliderect(elemento.lados["main"]):
                self.vidas += 1
                self.sonido_mas_vida = pygame.mixer.Sound("musica\Vidas.wav")
                self.sonido_mas_vida.play()
                lista_elementos.remove(elemento)
            else:
                elemento.update(pantalla)
        self.datos(pantalla)

    def datos(self, pantalla):
        # puntos = "Ataques\Sin Fondo_Frutilla.png"
        # imagen = pygame.image.load(puntos)  
        # imagen_redimensionada = pygame.transform.scale(imagen, (90, 40)) 
        
        # imagen_rect = imagen_redimensionada.get_rect()  
        # imagen_rect.x = 10  
        # imagen_rect.y = 10 
        crear_texto(pantalla, f"{self.contador_frutillas}", (200,10), (255, 255, 255), 20)
        # crear_texto(pantalla, f"VIDAS: {self.vidas}", (10, 10), color_blanco, 20)
        if self.vidas <= 0:
            imagen_path = "Vidas\Vidas_tres.png"  # Ruta de la imagen para 0 vidas o menos
        elif self.vidas == 1:
            imagen_path = "Vidas\Vidas_dos.png"  # Ruta de la imagen para 1 vida
        elif self.vidas == 2:
            imagen_path = "Vidas\Vidas_uno.png"  # Ruta de la imagen para 2 vidas
        elif self.vidas == 3:
            imagen_path = "Vidas\Vidas_Completas.png"  # Ruta de la imagen por defecto para más de 2 vidas
        elif self.vidas == 4:
            imagen_path = "Vidas\Vidas_Completas.png"

        imagen = pygame.image.load(imagen_path)  
        imagen_redimensionada = pygame.transform.scale(imagen, (90, 40)) 
        
        imagen_rect = imagen_redimensionada.get_rect()  
        imagen_rect.x = 10  
        imagen_rect.y = 10  

        
        pantalla.blit(imagen_redimensionada, imagen_rect)

    def trampas(self,pantalla, lista_trampas):
        if self.tiempo_invulnerable == 0:  
            for trampa in lista_trampas:
                if self.lados["main"].colliderect(trampa["main"]):
                    self.vidas -= 1
                    self.sonido_vidas = pygame.mixer.Sound("musica\Menos_vida.wav")
                    self.sonido_vidas.play()
                    self.tiempo_invulnerable = self.tiempo_invulnerable_total
                    break
        self.datos(pantalla)

    def restablecer_personaje(self):
        self.vidas = 3
        self.tiempo_invulnerable = 0
        rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        rectangulo.x = self.posicion_inicial[0]
        rectangulo.y = self.posicion_inicial[1]
        self.lados = obtener_rectangulo(rectangulo)  

    # def ubicacion_personaje(self):
    #     print("Posición actual del personaje: ({}, {})".format(self.lados["main"].x, self.lados["main"].y))
    
mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 8)









# def disparar_frutilla(self, posicion_personaje):
    #     frutilla = pygame.image.load("Ataques\Sin Fondo_Frutilla.png")  # Cargar la imagen de la frutilla
    #     tamaño_frutilla = reescalar_imagenes(frutilla, 10, 10)
    #     frutilla_rect = tamaño_frutilla.get_rect()  # Obtener el rectángulo de la frutilla
    #     frutilla_rect.center = posicion_personaje  # Establecer la posición inicial de la frutilla

    #     velocidad_frutilla = 5  # Velocidad de la frutilla

    #     direccion_x = -1 if self.bandera_izquierda else 1  # Determinar la dirección en el eje X

    #     frutilla_rect.x += velocidad_frutilla * direccion_x
    #     pantalla.blit(frutilla, frutilla_rect)










'''
def restablecer_personaje(self):
        self.vidas = 3
        self.tiempo_invulnerable = 0
        rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        rectangulo.x = self.posicion_inicial[0]
        rectangulo.y = self.posicion_inicial[1]
        self.lados = obtener_rectangulo(rectangulo)
'''

'''
laser:
posicion de personaje
moviento en ejes Y y X = valor que quiero y su velocidad
haci donde este mirando el personaje o donde este el mouse 

Disparos si miro a la izquierda + 
y si miro a la derecha - en el eje x
esto necesitara un nuevo def donde ejecutara estos disparos.
'''

