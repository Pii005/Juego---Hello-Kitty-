import pygame
import sys
from AA_Kitty import *
from Modulo import *
from CC_Pantalla import *
from DD_Plataformas import *
from AA_Enemigos import *
from CC_Recolectar import *
from CC_textos import *
from AA_trampas import *
import time

pygame.init()
pygame.font.init()

def movimientos():
    if keys[pygame.K_RIGHT]:
        mi_personaje.que_hace = "derecha"
    elif keys[pygame.K_LEFT]:
        mi_personaje.que_hace = "izquierda"
    elif keys[pygame.K_UP]:
        mi_personaje.que_hace = "salta"
    else:
        mi_personaje.que_hace = "quieto"
        
    if keys[pygame.K_e]:
        mi_personaje.que_hace = "Ataque_Frutilla"
    
    if keys[pygame.K_x]:
        mi_personaje.que_hace = "Ataque_Moño"




### MUSICA ###
# pygame.mixer.music.load("musica\Fondo.mp3")
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.5)




pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

while True:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo() 
        if evento.type == pygame.MOUSEBUTTONDOWN: #toco la pantalla
            print(evento.pos)
    keys = pygame.key.get_pressed()

    movimientos()

    pantalla.blit(fondo, (0, 0))  
    
    for trampa in listas_trampas:
        trampa.update(pantalla)

    contador_reloj(tiempo_inicial, pantalla)
    
    for plataforma in lista_plataformas:
        plataforma.animar(pantalla)

    # for plataforma in lista_plataformas_movimientos:
    #     plataforma.update_movimiento(pantalla)

    mi_personaje.update(pantalla, lista_gravedad, Enemigos, lista_objetos, lista_recuperar, lista_lados_trampas)
    
    for enemigo in Enemigos:
        enemigo.update(pantalla, lista_gravedad)

    

    if get_mode():
        for lado in mi_personaje.lados:
            pygame.draw.rect(pantalla, "Pink", mi_personaje.lados[lado], 2)
        # for lado in plataforma_uno[1]:
        #     pygame.draw.rect(pantalla, "Black", plataforma_uno[1][lado], 2)
        for lado in Humberto.lados:
            pygame.draw.rect(pantalla, "Pink", Humberto.lados[lado], 2)

    
    pygame.display.update()
