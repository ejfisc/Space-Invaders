import pygame, os
from pathlib import Path
pygame.font.init()
pygame.mixer.init()
# os.chdir(Path.home() / 'Space Invaders')

WIDTH, HEIGHT = 600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invaders')

PLAYER_WIDTH, PLAYER_HEIGHT = 50, 25
BULLET_WIDTH, BULLET_HEIGHT = 5, 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60
VEL = 4
BULLET_VEL = 7

def draw_window(bullets, player):
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
    # if keys_pressed[pygame.K_UP] and player.y - VEL > 0: # up
    #   player.y -= VEL
    # if keys_pressed[pygame.K_DOWN] and player.y + VEL + player.height < HEIGHT - 12: # down
    #   player.y += VEL

def handle_bullets(bullets, player):
    for bullet in bullets:
        bullet.y -= BULLET_VEL
        if bullet.y <= -10:
            bullets.remove(bullet)

def main():
    player = pygame.Rect(WIDTH//2 - (PLAYER_WIDTH//2), HEIGHT - (PLAYER_HEIGHT + 5), PLAYER_WIDTH, PLAYER_HEIGHT)
    bullets = []
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                bullet = pygame.Rect(player.x + PLAYER_WIDTH//2, player.y, BULLET_WIDTH, BULLET_HEIGHT)
                bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        handle_player_movement(keys_pressed, player)
        handle_bullets(bullets, player)
        draw_window(bullets, player)

if __name__ == '__main__':
    main()