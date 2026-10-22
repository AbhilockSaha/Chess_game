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
    pieces = ["wp","wR","wN","wB","wQ","wK","wB","wN","wR" ,"bp","bR","bN","bB","bQ","bK","bB","bN","bR"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("photo/" + piece + ".png"),(SQ_SIZE,SQ_SIZE))

'''
this main driver handel user input and update
'''

def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.file(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()

def drawGameState(screen,gs):
    drawBoard(screen) # draw square on the board
    drawPices(screen) # draw pices

if __name__ == "__main__":
    main()