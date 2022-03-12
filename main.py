import pygame, os
from pathlib import Path
pygame.font.init()
pygame.mixer.init()
# os.chdir(Path.home() / 'Space Invaders')

WIDTH, HEIGHT = 600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invaders')

TITLE_FONT = pygame.font.Font(str(Path('Assets', 'space_invaders.ttf')), 50)

PLAYER_WIDTH, PLAYER_HEIGHT = 50, 25
BULLET_WIDTH, BULLET_HEIGHT = 5, 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60
VEL = 4
BULLET_VEL = 7

TOP_SCORES = []

# HOME SCREEN

def draw_menu():
    WIN.fill(BLACK)
    title = TITLE_FONT.render('SPACE INVADERS', 1, WHITE)
    WIN.blit(title, (WIDTH//2 - title.get_width()//2, 50))
    pygame.display.update()

def menu():
    menu_state = True
    while menu_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game()

        draw_menu()

# GAME

def draw_game(bullets, player):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, player)
    for bullet in bullets:
        pygame.draw.rect(WIN, WHITE, bullet)
    pygame.display.update()

def handle_player_movement(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT] and player.x - VEL > 5: # left
        player.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and player.x + VEL + player.width < WIDTH - 5: # right
        player.x += VEL

def handle_bullets(player_bullets, player):
    for bullet in player_bullets:
        bullet.y -= BULLET_VEL
        if bullet.y <= -10:
            player_bullets.remove(bullet)

def game():
    player = pygame.Rect(WIDTH//2 - (PLAYER_WIDTH//2), HEIGHT - (PLAYER_HEIGHT + 5), PLAYER_WIDTH, PLAYER_HEIGHT)
    player_bullets = []
    score = 0
    clock = pygame.time.Clock()
    game_state = True
    while game_state:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = False
                pygame.quit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                bullet = pygame.Rect(player.x + PLAYER_WIDTH//2, player.y, BULLET_WIDTH, BULLET_HEIGHT)
                player_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        handle_player_movement(keys_pressed, player)
        handle_bullets(player_bullets, player)
        draw_game(player_bullets, player)

if __name__ == '__main__':
    menu()