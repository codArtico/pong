from configs import *
import pygame
class Menu:
    def __init__(self, tela, menu):
        self.tela = tela
        self.menu = menu

    def desenharMenu(self,tela,mainMenu):
        self.tela.blit(mainMenu,(0,0))
        pygame.draw.rect(tela, cores['barrinha'], pygame.Rect(800, 200, 200, 100))  # Exemplo com largura 200 e altura 100

        area_iniciar = (480 + 37, 120 + 220, 540, 130)
        area_sair = (480 + 37, 270 + 220, 540, 130)
        return area_iniciar, area_sair

    def click_botao(self, area, mouse_x, mouse_y):
        return area[0] <= mouse_x <= area[0] + area[2] and area[1] <= mouse_y <= area[1] + area[3]