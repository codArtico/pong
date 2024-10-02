from configs import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, nump):
        super().__init__(groups)
        self.nump = nump

        self.image = pygame.Surface(tamanhos['barrinha'])
        self.image.fill(cores['barrinha'])

        if nump == 1:
            self.rect = self.image.get_rect(center = pos['player1'])
        else:
            self.rect = self.image.get_rect(center = pos['player2'])
        self.direcao = 0
        self.velocidade = velocidades['barrinha']

    def move(self,dt):
        self.rect.centery += self.direcao * self.velocidade * dt
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.bottom = telaAltura if self.rect.bottom > telaAltura else self.rect.bottom
    
    def getDirecao(self):
        keys = pygame.key.get_pressed()

        if self.nump == 1:
            direcao_cima = int(keys[pygame.K_UP])
            direcao_baixo = int(keys[pygame.K_DOWN])
        else:
            direcao_cima = int(keys[pygame.K_w])
            direcao_baixo = int(keys[pygame.K_s])
        self.direcao = direcao_baixo - direcao_cima

    def update(self, dt):
        self.getDirecao()
        self.move(dt)