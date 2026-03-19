import pygame
from settings import BLACK

class Bullet:
    def __init__(self, pos, direction, owner):
        self.pos = pos.copy()
        self.dir = direction.normalize() if direction.length() > 0 else pygame.Vector2(1,0)
        self.owner = owner
        self.speed = 7

    def update(self):
        self.pos += self.dir * self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, BLACK, self.pos, 5)