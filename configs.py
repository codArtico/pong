import pygame
from os.path import join

telaLargura, telaAltura = 1280,720
fps = 30

tamanhos = {
    'barrinha':(40,100) , 'bola':(30,30),
}
velocidades = {
    'barrinha': 500, 'bola':450
}
cores = {
    'barrinha' : (0,0,0),
    'bg' : (255,255,255),
    'bola' : (255,0,0),
}