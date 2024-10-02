from configs import *
from sprites import *

class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((telaLargura, telaAltura))
        pygame.display.set_caption("Pong")
        self.fps = pygame.time.Clock()
        self.running = True

        #Sprites
        self.sprites = pygame.sprite.Group()
        self.barrinhaSprites = pygame.sprite.Group()

    def run(self):
        
        while self.running:
            
            dt = self.fps.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Atualizar sprites 
            self.sprites.update(dt)

            self.tela.fill(cores['bg'])
            self.sprites.draw(self.tela)

            pygame.display.update()

        pygame.quit()

    
if __name__ == "__main__":
    jogo = Jogo()
    jogo.run()