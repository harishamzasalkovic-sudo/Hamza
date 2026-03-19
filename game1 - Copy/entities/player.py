import pygame
from settings import RED, WIDTH, HEIGHT
from utils import get_rect, collides
from entities.bullet import Bullet

class Player:
    def __init__(self):
        self.pos = pygame.Vector2(100, HEIGHT//2)
        self.dir = pygame.Vector2(1, 0)
        self.speed = 4
        self.hp = 3
        self.shoot_cd = 0
        self.size = 30

    def update(self, keys):
        if self.shoot_cd > 0:
            self.shoot_cd -= 1

        move = pygame.Vector2(
            keys[pygame.K_d] - keys[pygame.K_a],
            keys[pygame.K_s] - keys[pygame.K_w]
        )

        if move.length() > 0:
            move = move.normalize()
            self.dir = move

            self.pos.x += move.x * self.speed
            if collides(get_rect(self.pos, self.size)):
                self.pos.x -= move.x * self.speed

            self.pos.y += move.y * self.speed
            if collides(get_rect(self.pos, self.size)):
                self.pos.y -= move.y * self.speed

        self.pos.x = max(15, min(WIDTH-15, self.pos.x))
        self.pos.y = max(15, min(HEIGHT-15, self.pos.y))

    def shoot(self, bullets):
        if self.shoot_cd == 0 and self.dir.length() > 0:
            bullets.append(Bullet(self.pos, self.dir, "player"))
            self.shoot_cd = 15

    def draw(self, screen):
        if self.hp > 0:
            pygame.draw.rect(screen, RED, get_rect(self.pos, self.size))
            pygame.draw.line(screen, (0,0,0), self.pos, self.pos + self.dir * 25, 3)