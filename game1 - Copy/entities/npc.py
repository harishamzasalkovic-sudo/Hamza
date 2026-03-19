import pygame
from settings import BLUE
from utils import get_rect
from entities.bullet import Bullet

class NPC:
    def __init__(self, height):
        self.pos = pygame.Vector2(650, height//2)
        self.hp = 3
        self.timer = 0
        self.size = 30

    def update(self, player, bullets):
        if self.hp <= 0:
            return

        self.timer += 1
        if self.timer > 60:
            self.timer = 0
            direction = player.pos - self.pos
            if direction.length() > 0:
                bullets.append(Bullet(self.pos, direction, "npc"))

    def draw(self, screen):
        if self.hp > 0:
            pygame.draw.rect(screen, BLUE, get_rect(self.pos, self.size))