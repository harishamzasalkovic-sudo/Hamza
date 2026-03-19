import pygame
from settings import *

class Scoreboard:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 50)
        self.score_p1 = 0
        self.score_p2 = 0

    def add_point_p1(self):
        self.score_p1 += 1

    def add_point_p2(self):
        self.score_p2 += 1

    def draw(self, screen):
        text = f"Spieler 1 = {self.score_p1}     Spieler 2 = {self.score_p2}"
        rendered = self.font.render(text, True, BLACK)

        # Zentriert in der Mitte oben
        rect = rendered.get_rect(center=(WIDTH // 2, 40))
        screen.blit(rendered, rect)