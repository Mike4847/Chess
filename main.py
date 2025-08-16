import pygame as Pyg
from chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENTION = 8

SQ_SIZE = HEIGHT // DIMENTION
IMAGES = {}
FPS= 15


def load_images():
    """
    loading and scalling the image to fit the square
    """
    pieces = ['bB','bK','bN','bp','bQ','bR','wB','wK','wN','wp','wQ','wR']
    for piece in pieces:
        IMAGES[piece]= Pyg.transform.scale(Pyg.image.load(f"chess/images/{piece}.png"),(SQ_SIZE, SQ_SIZE) )

def DrawGameState(screen, gameState):
    DrawBoard(screen)
    DrawPieces(screen , gameState.board)
    


def DrawBoard(screen):
    for row in range(DIMENTION):
        for column in range(DIMENTION):
            if (column+ row ) % 2 == 0:
                colour = (242, 223, 10)
            else:
                
                colour = (59, 29, 13)

            
            Pyg.draw.rect(screen, colour, (column *SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            
            



def DrawPieces(screen , board):
    for row in range(DIMENTION):
        for column in range(DIMENTION):
            piece = board[row][column]

            if (piece !="0"):
                screen.blit(IMAGES[piece], Pyg.Rect(column* SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def main()->None:
    Pyg.init()
    screen = Pyg.display.set_mode((WIDTH, HEIGHT))
    clock = Pyg.time.Clock()
    screen.fill("white")
    gameState = ChessEngine.GameState()
    load_images()
    Running = True
    while Running:
        #loop to poll the event queue
        for event in Pyg.event.get():
            if event.type == Pyg.QUIT:
                Running = False
        DrawGameState(screen, gameState)
        clock.tick(FPS)
        Pyg.display.flip()

    


#driver code 
if __name__ == "__main__":
    main()