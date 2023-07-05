import pygame
from pygame.locals import *

from GUI_button import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_form import *
from GUI_button_image import *

from menu_ajustes import *
from menu_niveles import *

# from AAC_Form_menu_score import *


class inicio:
    def __init__(self, screen):
        self.pantalla = screen

        self.btn_niveles = Button_Image(self.pantalla, 100, 100, 686, 456, 120, 40, "Menu\Inicio_opciones.jpg", self.play, "cualquier cosa")
        self.btn_ajustes = Button_Image(self.pantalla, 100, 100, 686, 514, 120, 40, "Menu\Salir_opciones.png", self.play, "cualquier cosa")

        self.lista_widgets = []
        self.lista_widgets.append(self.btn_niveles)
        self.lista_widgets.append(self.btn_ajustes)


    def play(self):
        ajutes = FormAjustes(self.pantalla, 250, 25, 500, 550, (220,0,220), "Pink", True, "Menu\Fondo_menu.jpg")
        self.show_dialog(ajutes)


    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                for widget in self.lista_widgets: #por cada widget en la lista lo dibujo
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)