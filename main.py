from configs import *
from sprites import *
from menus import *

class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((telaLargura, telaAltura))
        pygame.display.set_caption("Pong")
        self.fps = pygame.time.Clock()
        self.running = True
        self.bg = pygame.image.load(bgCaminho)
        self.mainMenu = pygame.image.load(mainMenuCaminho)
        self.menu = Menu(self.tela, mainMenuCaminho)

        #Sprites
        self.sprites = pygame.sprite.Group()
        self.barrinhaSprites = pygame.sprite.Group()
        self.player1 = Player((self.sprites, self.barrinhaSprites),1)
        self.bola = Bola(self.sprites, self.barrinhaSprites,self.gol)
        #self.player2 = Player((self.sprites, self.barrinhaSprites),2) Jogável
        self.player2 = IA((self.sprites, self.barrinhaSprites),2,self.bola) #IA

        #Placar
        self.placar = {'player1':0,'player2':0}
        self.font = pygame.font.Font(None,160)


    def mostrarPlacar(self):
        player1_surf = self.font.render(str(self.placar['player1']),True,cores['placar'])
        player1_rect = player1_surf.get_rect(center=(telaLargura//2+250, telaAltura//2))
        self.tela.blit(player1_surf, player1_rect)

        player2_surf = self.font.render(str(self.placar['player2']),True,cores['placar'])
        player2_rect = player2_surf.get_rect(center=(telaLargura//2-250, telaAltura//2))
        self.tela.blit(player2_surf, player2_rect)

    def gol(self, lado):
        if lado == 'player1':
            self.placar['player1'] += 1
        elif lado == 'player2':
            self.placar['player2'] += 1

    def run(self):
        
        while self.running:
            
            dt = self.fps.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Atualizar sprites
            
            
            self.sprites.update(dt)
            

            self.menu.desenharMenu(self.tela,self.mainMenu)
            while False:
                self.tela.blit(self.bg,(0,0))
                self.mostrarPlacar()
                self.sprites.draw(self.tela)
            

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    jogo = Jogo()
    jogo.run()