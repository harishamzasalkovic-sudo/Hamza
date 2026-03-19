import pygame
from settings import GREEN, WIDTH, HEIGHT
from utils import get_rect, collides

class KnifePlayer:
    def __init__(self):
        self.pos = pygame.Vector2(650, HEIGHT//2)
        self.speed = 5
        self.hp = 3
        self.attack_cd = 0
        self.size = 30

    def update(self, keys, player):
        if self.attack_cd > 0:
            self.attack_cd -= 1

        move = pygame.Vector2(
            keys[pygame.K_RIGHT] - keys[pygame.K_LEFT],
            keys[pygame.K_DOWN] - keys[pygame.K_UP]
        )

        if move.length() > 0:
            move = move.normalize()

            self.pos.x += move.x * self.speed
            if collides(get_rect(self.pos, self.size)):
                self.pos.x -= move.x * self.speed

            self.pos.y += move.y * self.speed
            if collides(get_rect(self.pos, self.size)):
                self.pos.y -= move.y * self.speed

        self.pos.x = max(15, min(WIDTH-15, self.pos.x))
        self.pos.y = max(15, min(HEIGHT-15, self.pos.y))

        if keys[pygame.K_KP1] and self.attack_cd == 0:
            self.attack_cd = 40
            if self.pos.distance_to(player.pos) < 40:
                player.hp -= 1

    def draw(self, screen):
        if self.hp > 0:
            pygame.draw.rect(screen, GREEN, get_rect(self.pos, self.size))