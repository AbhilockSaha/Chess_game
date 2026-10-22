
import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

# Load chess piece images
def loadImages():
    pieces = [
        "wp", "wR", "wN", "wB", "wQ", "wK",
        "bp", "bR", "bN", "bB", "bQ", "bK"
    ]

    for piece in pieces:
        IMAGES[piece] = p.transform.scale(
            p.image.load("photo/" + piece + ".png"),
            (SQ_SIZE, SQ_SIZE)
        )


# Main driver
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    p.display.set_caption("Chess Game")

    gs = ChessEngine.GameState()
    loadImages()

    running = True

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

    p.quit()


# Draw the complete game state
def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


# Draw the chessboard
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]

    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            p.draw.rect(screen,color,p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


# Draw the chess pieces
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]

            if piece != "--":
                screen.blit(IMAGES[piece],p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
