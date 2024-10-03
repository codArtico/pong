from configs import *
from random import choice, uniform

class Barrinha(pygame.sprite.Sprite):
    def __init__(self, groups, nump):
        super().__init__(groups)
        self.nump = nump
        self.pontuacao = 0
        self.image = pygame.Surface(tamanhos['barrinha'],pygame.SRCALPHA)
        pygame.draw.rect(self.image, cores['barrinha'], pygame.Rect((0, 0), tamanhos['barrinha']), border_radius=10)

        if nump == 1:
            self.rect = self.image.get_rect(center = pos['player1'])
            self.old_rect = self.rect.copy()
        else:
            self.rect = self.image.get_rect(center = pos['player2'])
            self.old_rect = self.rect.copy()
        self.direcao = 0
        
    def move(self,dt):
        self.rect.centery += self.direcao * self.velocidade * dt
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.bottom = telaAltura if self.rect.bottom > telaAltura else self.rect.bottom

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.getDirecao()
        self.move(dt)

class Player(Barrinha):
    def __init__(self, groups,nump):
        super().__init__(groups,nump)
        self.velocidade = velocidades['jogador']
    
    def getDirecao(self):
        keys = pygame.key.get_pressed()

        if self.nump == 2:
            direcao_cima = int(keys[pygame.K_UP])
            direcao_baixo = int(keys[pygame.K_DOWN])
        else:
            direcao_cima = int(keys[pygame.K_w])
            direcao_baixo = int(keys[pygame.K_s])
        self.direcao = direcao_baixo - direcao_cima

class IA(Barrinha):
    def __init__(self, groups, nump,bola):
        super().__init__(groups,nump)
        self.velocidade = velocidades['IA']
        self.bola = bola
    def getDirecao(self):
        self.direcao = 1 if self.bola.rect.centery > self.rect.centery else -1


class Bola(pygame.sprite.Sprite):
    def __init__(self, groups, barrinhaSprites, gol):
        super().__init__(groups)
        self.barrinhaSprites = barrinhaSprites
        self.gol = gol

        self.image = pygame.Surface(tamanhos['bola'], pygame.SRCALPHA)
        pygame.draw.circle(self.image, cores['bola'], (tamanhos['bola'][0] // 2, tamanhos['bola'][1] // 2), tamanhos['bola'][0] // 2)

        self.rect = self.image.get_rect(center=pos['bola'])
        self.old_rect = self.rect.copy()
        self.direction = pygame.Vector2(choice([1, -1]), uniform(0.7, 0.8) * choice([-1, 1]))

    def move(self, dt):
        self.rect.x += self.direction.x * velocidades['bola'] * dt
        self.colisao('horizontal')
        self.rect.y += self.direction.y * velocidades['bola'] * dt
        self.colisao('vertical')

    def reset(self):
        self.rect.center = pos['bola']
        self.direction = pygame.Vector2(choice([1, -1]), uniform(0.7, 0.8) * choice([-1, 1]))

    def colisao(self, direction):
        for sprite in self.barrinhaSprites:
            if sprite.rect.colliderect(self.rect):
                if direction == 'horizontal':
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                        self.direction.x *= -1
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                        self.direction.x *= -1
                else:
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                        self.direction.y *= -1
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                        self.direction.y *= -1

    def colisaoParede(self):
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y *= -1

        if self.rect.bottom >= telaAltura:
            self.rect.bottom = telaAltura
            self.direction.y *= -1

        
        if self.rect.left <= 0:
            self.gol('player2')
            self.reset()
        elif self.rect.right >= telaLargura:
            self.gol('player1')
            self.reset()

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.move(dt)
        self.colisaoParede()