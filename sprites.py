from configs import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, x_pos):
        super().__init__(groups)

        self.imagem = pygame.Surface(tamanhos['barrinha'])

        self.rect = self.imagem.get_frect(center = (x_pos,telaAltura/2))