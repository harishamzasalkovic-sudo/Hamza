import pygame
from settings import walls

def get_rect(pos, size):
    return pygame.Rect(pos.x - size//2, pos.y - size//2, size, size)

def collides(rect):
    return any(rect.colliderect(w) for w in walls)