from configs import *
from random import choice, uniform

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, nump):
        super().__init__(groups)
        self.nump = nump

        self.image = pygame.Surface(tamanhos['barrinha'],pygame.SRCALPHA)
        pygame.draw.rect(self.image, cores['barrinha'], pygame.Rect((0, 0), tamanhos['barrinha']), border_radius=10)

        if nump == 1:
            self.rect = self.image.get_rect(center = pos['player1'])
            self.old_rect = self.rect.copy()
        else:

            self.rect = self.image.get_rect(center = pos['player2'])
            self.old_rect = self.rect.copy()
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
        self.old_rect = self.rect.copy()
        self.getDirecao()
        self.move(dt)

class Bola(pygame.sprite.Sprite):
    def __init__(self, groups, barrinhaSprites):
        super().__init__(groups)
        self.barrinhaSprites = barrinhaSprites

        self.image = pygame.Surface(tamanhos['bola'], pygame.SRCALPHA)
        pygame.draw.circle(self.image,cores['bola'],(tamanhos['bola'][0]/2,tamanhos['bola'][1]/2),tamanhos['bola'][0]/2)

        self.rect = self.image.get_rect(center = pos['bola'])
        self.old_rect = self.rect.copy()
        self.direction = pygame.Vector2((choice([1,-1])), uniform(0.7, 0.8) * choice([-1,1]))

    def move(self,dt):
        self.rect.x += self.direction.x * velocidades['bola'] * dt
        self.colisao('horizontal')
        self.rect.y += self.direction.y * velocidades['bola'] * dt
        self.colisao('vertical')



    def colisao(self, direction):
        for sprite in self.barrinhaSprites:
            if sprite.rect.colliderect(self.rect):
                if direction == 'horizontal':
                    # Colisão com o Player 1 (barrinha da direita)
                    if self.direction.x > 0:  # Bola indo para a direita
                        if self.rect.right > sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                            self.rect.right = sprite.rect.left
                            self.direction.x *= -1  # Invertendo a direção no eixo x

                    # Colisão com o Player 2 (barrinha da esquerda)
                    elif self.direction.x < 0:  # Bola indo para a esquerda
                        if self.rect.left < sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                            self.rect.left = sprite.rect.right
                            self.direction.x *= -1  # Invertendo a direção no eixo x


    
    def colisaoParede(self):
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y *= -1

        if self.rect.bottom >= telaAltura:
            self.rect.bottom = telaAltura
            self.direction.y *= -1

        if self.rect.left <= 0:
            self.rect.left = 0
            self.direction.x *= -1

        if self.rect.right >= telaLargura:
            self.rect.right = telaLargura
            self.direction.x *= -1

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.move(dt)
        self.colisaoParede()