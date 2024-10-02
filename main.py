from configs import *

class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((telaLargura, telaAltura))
        pygame.display.set_caption("Pong")
        self.fps = pygame.time.Clock()
        self.running = True

    def run(self):
        
        while self.running:
            self.tela.fill(cores['bg'])
            dt = self.fps.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()

        pygame.quit()

    
if __name__ == "__main__":
    jogo = Jogo()
    jogo.run()