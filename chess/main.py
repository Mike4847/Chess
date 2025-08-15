import pygame as Pyg
from chess import ChessEngine, images

WIDTH = HEIGHT = 512
DIMENTION = 8

SQ_SIZE = HEIGHT // DIMENTION
IMAGES = {}


def load_images():
    """
    loading and scalling the image to fit the square
    """
    pieces = ['bB','bK','bN','bp','bQ','bR','wB','wK','bN','wp','wQ','wR']
    for piece in pieces:
        IMAGES[piece]= Pyg.transform.scale(Pyg.image.load(f"images/{piece}.png"),(SQ_SIZE, SQ_SIZE) )
