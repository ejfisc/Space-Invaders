import pygame, os, random
from pathlib import Path
pygame.font.init()
pygame.mixer.init()
# os.chdir(Path.home() / 'Space Invaders')

# WINDOW
WIDTH, HEIGHT = 600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invaders')

# FONTS
TITLE_FONT = pygame.font.Font(str(Path('Assets', 'space_invaders.ttf')), 50)

# SOUNDS
BULLET_FIRE_SOUND = pygame.mixer.Sound(str(Path('Assets', 'player_shoot.mp3')))

# ENTITIES
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 25
BULLET_WIDTH, BULLET_HEIGHT = 5, 10
SHIELD_WIDTH, SHIELD_HEIGHT = 80, 8
ALIEN_WIDTH, ALIEN_HEIGHT = 40, 40
PLAYER_IMG = pygame.image.load(Path('Assets', 'player.png'))
PLAYER = pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT))

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# CONSTANTS
FPS = 60
VEL = 4
BULLET_VEL = 7
ALIEN_VEL = 1

# SCORE ARRAY
# TODO: write scores to a file, read them to a list, and sort them
top_scores = []

# CLOCK
clock = pygame.time.Clock()

# HOME SCREEN

# TODO:
# draw actual menu
# add background
# show controls
def draw_menu():
    WIN.fill(BLACK)
    title = TITLE_FONT.render('SPACE INVADERS', 1, WHITE)
    WIN.blit(title, (WIDTH//2 - title.get_width()//2, 50))
    pygame.display.update()

# TODO:
# select difficulty?
# button to start game
def menu(): 
    pygame.mixer.music.load(str(Path('Assets', 'menu.wav')))
    pygame.mixer.music.play(-1)
    menu_state = True
    while menu_state:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_state = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                menu_sate = False
                pygame.mixer.music.stop()
                game()

        draw_menu()

# GAME

# TODO:
# draw alien bullets
# draw health
# draw score
# add alien images
# draw hit combo score
def draw_game(bullets, player, score, keys_pressed, aliens):
    WIN.fill(BLACK)
    WIN.blit(PLAYER, (player.x, player.y))
    if keys_pressed[pygame.K_RSHIFT]:
        shield = pygame.Rect(player.x - 15, player.y - 15, SHIELD_WIDTH, SHIELD_HEIGHT)
        pygame.draw.rect(WIN, WHITE, shield)
    for bullet in bullets:
        pygame.draw.rect(WIN, WHITE, bullet)
    for alien in aliens:
        pygame.draw.rect(WIN, GREEN, alien)
    pygame.display.update()

def player_movement(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT] and player.x - VEL > 5: # left
        player.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and player.x + VEL + player.width < WIDTH - 5: # right
        player.x += VEL

# TODO:
# Fix it so the aliens don't collide with eachother
# remove alien when they collide with player shield
# decrease health when alien collides with player
def alien_movement(aliens, player):
    for alien in aliens:
        if player.x > alien.x: # alien is to the left of player
           alien.x += ALIEN_VEL
        if player.x < alien.x:
           alien.x -= ALIEN_VEL
        alien.y += ALIEN_VEL
        if alien.colliderect(player):
            aliens.remove(alien)
        
# TODO: 
# Add bullet hit sound
# Add alien bullets
# Decrease life when alien bullet hits player
# Remove alien bullet when bullet hits player shield
# increment score when player shoots the bonus coin
def handle_bullets(player_bullets, player, aliens):
    for bullet in player_bullets:
        bullet.y -= BULLET_VEL
        if bullet.y <= -10:
            player_bullets.remove(bullet)
        for alien in aliens:
            if alien.colliderect(bullet):
                player_bullets.remove(bullet)
                aliens.remove(alien)

# TODO:
# repopulate aliens after amount of time or alien deaths
def populate_aliens():
    aliens = []
    for i in range(0, 5):
        randx = random.randint(10, WIDTH - 50)
        randy = random.randint(10, 100)
        alien = pygame.Rect(randx, randy, ALIEN_WIDTH, ALIEN_HEIGHT)
        aliens.append(alien)
    return aliens

# TODO:
# add a bonus coin
# increment score when player kills an alien
# start combo when player kills an alien, and increment combo for each contiguous kill until the player misses
# save top scores
def game():
    pygame.mixer.music.load(str(Path('Assets', 'game.wav')))
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    player = pygame.Rect(WIDTH//2 - (PLAYER_WIDTH//2), HEIGHT - (PLAYER_HEIGHT + 5), PLAYER_WIDTH, PLAYER_HEIGHT)
    player_bullets = []
    aliens = populate_aliens()
    score = 0
    game_state = True

    while game_state:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = False
                pygame.quit()

            if keys_pressed[pygame.K_RSHIFT]:
                pass
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                BULLET_FIRE_SOUND.play()
                bullet = pygame.Rect(player.x + PLAYER_WIDTH//2, player.y, BULLET_WIDTH, BULLET_HEIGHT)
                player_bullets.append(bullet)
        
        player_movement(keys_pressed, player)
        alien_movement(aliens, player)
        handle_bullets(player_bullets, player, aliens)
        draw_game(player_bullets, player, score, keys_pressed, aliens)

if __name__ == '__main__':
    menu()