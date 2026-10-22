import pygame as p

import ChessEngine

WIDTH = HEIGHT = 512 
DIMENSION = 8

SQ_SIZE = HEIGHT // DIMENSION

MAX_FPS = 15 
IMAGES = {}

'''
Initializinf a global dictionary of images. This will be called exactly once in the main 
'''

def loadImages():
    piece = ["wP","wR","wN","wB","wQ","wK","wB","wN","wR"]
    IMAGES[piece] = p.image.load("photo/" + piece + ".png")