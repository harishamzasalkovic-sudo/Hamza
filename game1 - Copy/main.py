import pygame
import sys
import button
from settings import *
from scoreboard import Scoreboard
from entities.player import Player
from entities.knife_player import KnifePlayer

pygame.init()

# Fenster
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top Down Shooter")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont("arialblack", 40)
TEXT_COL = (255, 255, 255)

# Menu States
game_state = "menu"   # menu, pvp, 
game_paused = False
menu_state = "main"

# Button Bilder laden
start_img = pygame.image.load("C:\\Users\\andre\\Downloads\\game1 - Copy\\game1 - Copy\\buttons\\button_start.png").convert_alpha()
resume_img = pygame.image.load("C:\\Users\\andre\\Downloads\\game1 - Copy\\game1 - Copy\\buttons\\button_resume.png").convert_alpha()
quit_img = pygame.image.load("C:\\Users\\andre\\Downloads\\game1 - Copy\\game1 - Copy\\buttons\\button_quit.png").convert_alpha()
back_img = pygame.image.load("C:\\Users\\andre\\Downloads\\game1 - Copy\\game1 - Copy\\buttons\\button_back.png").convert_alpha()


# Buttons
start_button = button.Button(304, 200, start_img, 1)
resume_button = button.Button(304, 125, resume_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
back_button = button.Button(332, 450, back_img, 1)


# Spieler erstellen
player = Player()
knife = KnifePlayer()
bullets = []
Scoreboard = Scoreboard()

def draw_text(text, x, y):
    img = font.render(text, True, TEXT_COL)
    screen.blit(img, (x, y))


#  MAIN LOOP 
run = True
while run:
    clock.tick(FPS)
    screen.fill((52, 78, 91))

    #  MENU 
    if game_state == "menu":

        draw_text("TOP DOWN SHOOTER", 175, 100)

        if quit_button.draw(screen):
            run = False

        if start_button.draw(screen):
            game_state = "pvp"


    # GAME 
    else:

        if game_paused:
            draw_text("PAUSED", WIDTH//2 - 100, 50)

            if resume_button.draw(screen):
                game_paused = False

            if quit_button.draw(screen):
                game_state = "menu"
                game_paused = False
            
           

        else:
            keys = pygame.key.get_pressed()
            player.update(keys)

            # Schüsse updaten
            for bullet in bullets[:]:
                bullet.update()
                if not screen.get_rect().collidepoint(bullet.pos):
                    bullets.remove(bullet)

            # Zeichnen
            screen.fill(WHITE)

            for w in walls:
                pygame.draw.rect(screen, GRAY, w)

            Scoreboard.draw(screen)
             
            player.draw(screen)

            for bullet in bullets:
                bullet.draw(screen)


    # ================= EVENTS =================
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and game_state != "menu":
                game_paused = not game_paused

            if event.key == pygame.K_SPACE and not game_paused and game_state != "menu":
                player.shoot(bullets)

    pygame.display.update()

pygame.quit()
sys.exit()