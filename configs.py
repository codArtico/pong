import pygame
import os
from os.path import join

import os
import sys

def get_resource_path(relative_path):
    """ Função para obter o caminho do recurso, mesmo dentro de um executável """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Use a função para obter os caminhos das imagens
bgCaminho = get_resource_path(os.path.join('imagens', 'Quadra.jpg'))
mainMenuCaminho = get_resource_path(os.path.join('imagens', 'TelaInicial.jpg'))
iconCaminho = get_resource_path(os.path.join('imagens', 'quadra.ico'))


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
    'placar': (0,166,207)
}