import pygame
from pygame.locals import *

from GUI_button import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_form import *
from GUI_button_image import *



class FormAjustes(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image, margen_y):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        self._slave = aux_imagen
        self._margen_y = margen_y

        self.btn_play = Button(self._slave, x, y, 100, 100, 80, 20, "Red", "Brown", self.btn_play_click, "Nombre", "Pause",font = "Verdana", font_size=15, font_color="Black")
        ###LABEL - volumen ###
        self.label_volumen = Label(self._slave, 650, 190, 100, 50, "20%", "Comic Sans", 15, "Black", "Table.png")
        ###SLIDER###
        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 500, 15, self.volumen, "Blue", "Yellow")


        self.lista_widgets.append(self.btn_play) # guardo boton
        self.lista_widgets.append(self.label_volumen) #Guardo cuadro con volumen
        self.lista_widgets.append(self.slider_volumen)#agrego slider con barrita de volumen

        pygame.mixer.music.load("musica\Fondo.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

    def update(self, lista_eventos): # actualizar elementos en mi formulario
        if self.verificar_dialog_result():
            if self.active:
                self.draw() #DIBUJO el formulario
                self.render()#render, poner los objetos arriba del formulario
                for widget in self.lista_widgets: #por cada widget en la lista lo dibujo
                    widget.update(lista_eventos) # en la pantalla
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def btn_play_click(self, texto):
        # print(texto) me mostrara el texto que le puse -> nombre
        '''OBTENER TEXTO DE TXT BOX
        texto = self.txtbox.get_text()
        '''
        '''PARAR MUSICA'''
        if self.flag_play:
            pygame.mixer.music.pause() #pausar musica
            self.btn_play._color_background = "Cyan" #COLOR FONDO boton
            self.btn_play._font_color = "White" # COLOR texto
            self.btn_play.set_text("Play") #NUEVO MENSAJE
        else: #vuelvo a lo de antes
            pygame.mixer.music.unpause() # despausa musica
            self.btn_play._color_background = "Red" 
            self.btn_play._font_color = "Brown"
            self.btn_play.set_text("Pause")

        self.flag_play = not self.flag_play
    
    def update_volumen(self, lista_eventos): #AJUSTES DE VOLUMEN
        self.volumen = self.slider_volumen.value
        # self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

