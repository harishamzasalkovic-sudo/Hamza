import pygame

WIDTH, HEIGHT = 800, 600
FPS = 60

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
BLUE = (50, 50, 200)
GREEN = (50, 180, 50)
GRAY = (120, 120, 120)

pygame.init()
font = pygame.font.SysFont(None, 36)

# Wände
walls = [
    pygame.Rect(350, 100, 30, 400),
    pygame.Rect(200, 250, 200, 30),
]