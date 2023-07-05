import pygame
import sys
# from AA_Kitty import *
# from Modulo import *
# from CC_Pantalla import *
# from DD_Plataformas import *
# from AA_Enemigos import *
# from CC_Recolectar import *
# from CC_textos import *
# from AA_trampas import *
import sys
# from GUI_button_image import *
# from GUI_textbox import *

from menu import inicio

W, H = 1500, 900
TAMAÑO_PANTALLA = (W, H)
FPS = 20

RELOJ = pygame.time.Clock()
pantalla = pygame.display.set_mode(TAMAÑO_PANTALLA)


pygame.init()
# pygame.font.init()
pygame.display.set_caption("Hello Kitty Adventure")
icono = pygame.image.load("Fotos\Logo.png")
pygame.display.set_icon(icono)

# Fondo
fondo = pygame.image.load("Menu\Fondo_menu.jpg")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)

#self.btn_tabla = Button_Image(self._slave, x, y, 255, 100, 50, 50, "Menu_BTN.png", self.btn_tabla_click, "cualquier cosa")

# btn_play = Button_Image(pantalla, W/2, H/2,  255, 100, 50, 50, "Menu_BTN.png", btn_tabla_click(), "cualquier cosa")

# txtbox = TextBox(pantalla, 10, 10 ,50, 50, 150, 30, "Blue", "Orange", "Pink", "Red", 2, font = "Comic Sans", font_size=15, font_color= "Black")

# lista_widgets = []
# lista_widgets.append(txtbox)

play = inicio(pantalla)

while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # elif evento.type == pygame.KEYDOWN:
        #     if evento.key == pygame.K_TAB:
        #         cambiar_modo() 
        if evento.type == pygame.MOUSEBUTTONDOWN: #toco la pantalla
            print(evento.pos)
    keys = pygame.key.get_pressed()

    # movimientos()

    pantalla.blit(fondo, (0, 0))  
    
    
    play.update(eventos)

    # for widgets in lista_widgets:
    #     widgets.update(eventos)


    

    
    pygame.display.update()
