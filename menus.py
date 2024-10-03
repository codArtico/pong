from configs import *
import pygame
class Menu:
    def __init__(self, tela, menu):
        self.tela = tela
        self.menu = menu

    def desenharMenu(self,tela,mainMenu):
        self.tela.blit(mainMenu,(0,0))

        area_humanos = (460, 346, 337, 100)
        area_ia = (460, 481, 337, 100)
        return area_humanos, area_ia

    def click_botao(self, area, mouse_x, mouse_y):
        return area[0] <= mouse_x <= area[0] + area[2] and area[1] <= mouse_y <= area[1] + area[3]