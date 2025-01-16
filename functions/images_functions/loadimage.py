import pygame
import os

def load_image(pathh, name, color_key=None):
    fullname = os.path.join(pathh, name)
    
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print("Cannot load image:", name)
        raise SystemExit(message)

    image = pygame.image.load(fullname).convert_alpha()

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
        
    return image