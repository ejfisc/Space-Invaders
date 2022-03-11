import pygame, os
from pathlib import Path
pygame.font.init()
pygame.mixer.init()
# os.chdir(Path.home() / 'Space Invaders')

WIDTH, HEIGHT = 600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invaders')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60

def draw_window():
    WIN.fill(BLACK)
    pygame.display.update()

def main():
    draw_window()
    main()

if __name__ == '__main__':
    main()