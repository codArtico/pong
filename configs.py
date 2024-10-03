import pygame
from os.path import join

telaLargura, telaAltura = 1280,720
fps = 30

tamanhos = {
    'barrinha':(40,150) , 'bola':(30,30),
}

pos = {
    'player1':(50, telaAltura/2),
    'player2':(telaLargura-50, telaAltura/2),
    'bola':(telaLargura/2,telaAltura/2)
}
velocidades = {
    'jogador': 500, 'bola':450, 'IA': 250
}
cores = {
    'barrinha' : (0,0,0),
    'bg' : (255,255,255),
    'bola' : (255,0,0),
    'placar': (127,127,127)
}